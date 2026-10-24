#!/usr/bin/env python3
"""Build data/news.json from an export of the artifact DB "news" collection.

Usage: python3 tools/publish.py <export_dir_with_json_files> <lastRun ISO timestamp> [today YYYY-MM-DD]

- Each exported file is either the bare item or {"id":..., "data": {...}}.
- Items without "added" get today's (IST) date.
- Items are linked to a meeting from data/conferences.json: an explicit
  "conference" field (meeting id) wins; otherwise the meeting's "match" regex is
  tried against title, summary, key data and tags. Approvals and regulatory
  items are only linked when they say so explicitly.
- "session" (Presidential, Plenary, LBA, Oral, Poster, Preview, Presented) is
  inferred when missing.
- The meeting calendar is embedded as "conferences" so the app needs no extra download.
"""
import datetime as dt
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SESSION_ORDER = ["Presidential", "Plenary", "LBA", "Oral", "Mini-oral", "Poster", "Presented", "Analysis", "Preview"]


def ist_today():
    return (dt.datetime.now(dt.timezone.utc) + dt.timedelta(hours=5, minutes=30)).date().isoformat()


def infer_session(item, conf):
    hay = " ".join([item.get("title", ""), item.get("summary", ""), item.get("keyData", ""), " ".join(item.get("tags", []))])
    if (item.get("date") or "") < conf["start"] or re.search(
        r"will be presented|to be presented|will present|due (at|as)|expected at|slated for|data come at|readouts to watch|on (the )?programme", hay, re.I
    ):
        pre = True
    else:
        pre = False
    if re.search(r"presidential", hay, re.I):
        return "Presidential"
    if re.search(r"plenary", hay, re.I):
        return "Plenary"
    if re.search(r"\bLBA\d*\b|late[- ]break", hay, re.I):
        return "LBA"
    if pre:
        return "Preview"
    if re.search(r"mini[- ]oral", hay, re.I):
        return "Mini-oral"
    if re.search(r"\boral\b|proffered", hay, re.I):
        return "Oral"
    if re.search(r"poster", hay, re.I):
        return "Poster"
    return "Presented"


def link(items, confs):
    by_id = {c["id"]: c for c in confs}
    pats = [(c, re.compile(c["match"], re.I)) for c in confs if c.get("match")]
    for it in items:
        conf = by_id.get(it.get("conference"))
        if not conf:
            it.pop("conference", None)
            hay = " ".join([it.get("title", ""), it.get("summary", ""), it.get("keyData", ""), " ".join(it.get("tags", []))])
            strict = it.get("category") in ("approval", "regulatory")
            for c, rx in pats:
                if rx.search(hay):
                    if strict and not re.search(r"presented at|presentation at", hay, re.I):
                        continue
                    conf = c
                    break
        if conf:
            it["conference"] = conf["id"]
            if it.get("session") not in SESSION_ORDER:
                it["session"] = infer_session(it, conf)
            # A preview becomes "Presented" automatically once the meeting is over.
            if it["session"] == "Preview" and ist_today() > (conf.get("end") or conf["start"]):
                it["session"] = "Presented"
    return items


def main():
    src, last_run = sys.argv[1], sys.argv[2]
    today = sys.argv[3] if len(sys.argv) > 3 else ist_today()
    items = []
    for f in sorted(glob.glob(os.path.join(src, "*.json"))):
        x = json.load(open(f))
        it = x.get("data", x)
        it["id"] = x.get("id") or os.path.basename(f)[:-5]
        it.setdefault("added", today)
        items.append(it)
    cal = json.load(open(os.path.join(ROOT, "data", "conferences.json")))
    confs = sorted(cal["conferences"], key=lambda c: c["start"])
    link(items, confs)
    items.sort(key=lambda i: (i.get("added", ""), i.get("date", "")), reverse=True)
    out = {"updated": last_run, "items": items, "conferences": confs}
    with open(os.path.join(ROOT, "data", "news.json"), "w") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    linked = sum(1 for i in items if i.get("conference"))
    print(f"{len(items)} items, {linked} linked to {len({i['conference'] for i in items if i.get('conference')})} meetings")


if __name__ == "__main__":
    main()
