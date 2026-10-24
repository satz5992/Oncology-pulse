"""Lists trials whose appraisal is too thin (used while writing; not part of the build)."""
import json
G = {"prior therapy", "none", "prior systemic therapy", "prior chemotherapy", "prior rt"}
t = json.load(open("data/trials.json"))["trials"]
bad = []
for d in t:
    a = d.get("appraisal", {})
    spec_exc = [x for x in a.get("exclusion", []) if x.lower() not in G]
    if (len(a.get("critique", "")) < 90 or len(a.get("inclusion", [])) < 2 or len(spec_exc) < 2
            or len(a.get("strengths", [])) < 2 or len(a.get("limitations", [])) < 2):
        bad.append(d["name"])
print(len(bad)); print(bad)
