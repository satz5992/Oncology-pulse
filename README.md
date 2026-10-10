# Oncology Pulse

A personal Android app with a daily feed of oncology drug approvals, trial results, FDA designations and upcoming regulatory decisions.

## Install
Open the **Releases** page of this repository on your phone, download `OncologyPulse.apk` from the "latest" release and open it. Android will ask you to allow installs from your browser the first time.

## How it works
- `data/news.json` holds the feed. A scheduled Claude task adds new items every morning (around 6:49 am IST) and pushes the updated file here.
- The app downloads `data/news.json` when opened, keeps a copy for offline reading, and checks in the background every few hours, sending a notification when new items arrive.
- Any change under `app/` rebuilds the APK automatically with GitHub Actions and replaces the file on the "latest" release. New builds install over the old one.

## Feed format
```json
{ "updated": "2026-10-10T01:30:00Z",
  "items": [ { "id": "2026-10-09-slug", "title": "...", "summary": "...", "keyData": "...",
               "category": "approval|trial|designation|regulatory|upcoming|research",
               "tumor": "Breast", "date": "2026-10-09", "impact": "notable|practice-changing",
               "source": "...", "url": "...", "tags": ["..."],
               "actionDate": "2026-11-30", "actionDateLabel": "30 Nov" } ] }
```

Summaries are compiled automatically; confirm against the original publication or label before clinical use.
