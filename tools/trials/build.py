"""Builds data/trials.json from the per-site modules in this folder."""
import json, re, importlib, sys, os
sys.path.insert(0, os.path.dirname(__file__))
FIELDS = ["name","setting","modality","year","journal","design","population","arms","endpoint","result","takeaway","tags"]
ORDER = ["Breast","Lung","Oesophagus & Stomach","Colorectal","Anal","Pancreas","Hepatobiliary","Neuroendocrine",
         "Prostate","Bladder & Upper Tract","Kidney","Testis","Gynaecologic","Head & Neck","CNS",
         "Myeloma","Lymphoma","Leukaemia & MDS","Melanoma & Skin","Sarcoma & GIST",
         "Radiotherapy (general & palliative)","Supportive care"]
sites = {}
for mod in ["breast","lung","gi","gu_gyn","other"]:
    m = importlib.import_module(mod)
    if hasattr(m, "TRIALS"): sites.setdefault(m.SITE, []).extend(m.TRIALS)
    for k, v in getattr(m, "TRIALS_BY_SITE", {}).items(): sites.setdefault(k, []).extend(v)
out, seen = [], set()
for site in ORDER:
    for t in sites.pop(site, []):
        assert len(t) == len(FIELDS), (site, t[0], len(t))
        d = dict(zip(FIELDS, t)); d["site"] = site
        slug = re.sub(r"[^a-z0-9]+", "-", d["name"].lower()).strip("-")[:60]
        assert slug not in seen, slug; seen.add(slug); d["id"] = slug
        out.append(d)
assert not sites, sites.keys()
root = os.path.join(os.path.dirname(__file__), "..", "..")
json.dump({"version": 1, "updated": "2026-10-10", "count": len(out), "trials": out},
          open(os.path.join(root, "data", "trials.json"), "w"), ensure_ascii=False, indent=1)
from collections import Counter
print(len(out)); print(Counter(d["site"] for d in out))
