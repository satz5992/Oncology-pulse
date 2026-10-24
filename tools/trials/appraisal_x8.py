# Depth pass: gynaecologic and head & neck.
A = {}
def add(name, inc, exc, pros, cons, critique):
    A[name] = {"inclusion": inc, "exclusion": exc, "strengths": pros, "limitations": cons, "critique": critique}

add("GOG 111 / OV-10",
    ["Stage III–IV ovarian cancer after surgery", "GOG 111: suboptimally debulked"],
    ["Prior chemotherapy", "Borderline tumours"],
    ["OS benefit for paclitaxel", "Confirmed in OV-10"],
    ["Cisplatin toxicity", "Later replaced by carboplatin"],
    "Established platinum-paclitaxel as standard first-line chemotherapy for ovarian cancer.")

add("GOG 172 (Armstrong IP)",
    ["Optimally debulked (≤1 cm) stage III ovarian cancer", "GOG PS 0–2"],
    ["Prior chemotherapy", "Suboptimal debulking"],
    ["OS benefit (~16 months)", "Long-term follow-up"],
    ["Toxicity and catheter complications", "Only 42% completed 6 cycles IP"],
    "IP chemotherapy improves OS but is rarely used due to toxicity and complexity; GOG 252 did not confirm benefit with modified regimens.")

add("JGOG 3016",
    ["Stage II–IV ovarian cancer", "Japanese patients"],
    ["Prior chemotherapy", "Borderline tumours"],
    ["OS benefit with dose-dense paclitaxel", "Long-term follow-up"],
    ["Not replicated in Western trials (ICON8)", "Anaemia"],
    "Dose-dense paclitaxel is an option, mainly in Asian patients.")

add("EORTC 55971 / CHORUS",
    ["Stage IIIC–IV ovarian cancer", "Suitable for either approach"],
    ["Prior therapy", "Non-epithelial tumours"],
    ["Non-inferior OS with NACT", "Less surgical morbidity"],
    ["Low complete resection rates", "Short survival overall"],
    "NACT is acceptable for high tumour burden or poor-performance patients.")

add("OVHIPEC-1",
    ["Stage III ovarian cancer after 3 cycles NACT", "Not eligible for primary surgery"],
    ["Prior HIPEC", "Extra-abdominal disease"],
    ["OS benefit", "Randomised"],
    ["Open-label", "Small trial (n=245)"],
    "HIPEC at interval debulking is an option in experienced centres.")

add("SOLO-1",
    ["BRCA-mutated advanced ovarian cancer responding to platinum", "High-grade serous or endometrioid"],
    ["Prior PARP inhibitor", "MDS/AML"],
    ["Large PFS and OS benefit", "Long-term follow-up"],
    ["Limited to BRCA-mutated", "Myelosuppression"],
    "Olaparib maintenance is standard for BRCA-mutated.")

add("PAOLA-1",
    ["Advanced ovarian cancer after platinum + bevacizumab", "High-grade serous or endometrioid"],
    ["Prior PARP inhibitor", "MDS/AML"],
    ["PFS and OS benefit in HRD-positive", "Biomarker-driven"],
    ["Little benefit in HRD-negative", "Requires HRD testing"],
    "Olaparib + bevacizumab is standard for HRD-positive.")

add("PRIMA",
    ["Advanced ovarian cancer responding to first-line platinum", "High-risk features"],
    ["Prior PARP inhibitor", "MDS/AML"],
    ["PFS benefit across biomarker groups", "Included high-risk patients"],
    ["No OS benefit", "Thrombocytopenia"],
    "Niraparib is an option across biomarker groups.")

add("ICON7 / GOG 218",
    ["Advanced ovarian cancer", "High-risk early-stage (ICON7)"],
    ["Prior therapy", "Bowel obstruction"],
    ["PFS benefit", "OS benefit in high-risk subgroup"],
    ["OS benefit only in high-risk subgroup", "Hypertension, GI perforation"],
    "Bevacizumab is an option for high-risk disease.")

add("MIRASOL",
    ["FRα-high platinum-resistant ovarian cancer", "1–3 prior lines"],
    ["Prior mirvetuximab", "Corneal disorders"],
    ["OS benefit", "Biomarker-driven"],
    ["Ocular toxicity", "Requires FRα testing"],
    "Mirvetuximab is standard for FRα-high PROC.")

add("PORTEC-1/2",
    ["Intermediate/high-intermediate-risk endometrial cancer", "After hysterectomy"],
    ["High-risk features", "Stage III–IV"],
    ["Reduced local recurrence", "Less toxicity with brachytherapy"],
    ["No OS benefit", "Pre-molecular era"],
    "Vaginal brachytherapy is standard for HIR.")

add("PORTEC-3",
    ["High-risk endometrial cancer", "Stage I–III"],
    ["Prior therapy", "Distant metastases"],
    ["Improved OS", "Benefit in serous and stage III"],
    ["Toxicity", "Long-term neuropathy"],
    "ChemoRT is standard for high-risk endometrial cancer.")

add("GOG 258",
    ["Stage III–IVA endometrial cancer", "After surgery"],
    ["Prior therapy", "Distant metastases"],
    ["No OS benefit for chemoRT", "Large trial"],
    ["Locoregional benefit", "Toxicity"],
    "Chemotherapy alone is standard; chemoRT improves local control.")

add("RUBY / NRG-GY018",
    ["Stage III–IV or recurrent endometrial cancer", "Measurable disease"],
    ["Prior immunotherapy", "Active autoimmune disease"],
    ["PFS benefit, OS in dMMR", "Two concordant trials"],
    ["Limited benefit in pMMR", "Immune toxicity"],
    "Chemo-IO is standard, especially for dMMR.")

add("KEYNOTE-775",
    ["Advanced endometrial cancer after platinum", "Any MMR status"],
    ["Prior lenvatinib", "Uncontrolled hypertension"],
    ["OS benefit", "Benefit in pMMR"],
    ["Toxicity (hypertension, fatigue)", "Dose reductions common"],
    "Lenvatinib-pembrolizumab is second-line standard.")

add("Cervix chemoRT (Rose / Morris, 1999 NCI alert)",
    ["Locally advanced cervical cancer", "FIGO IB2–IVA"],
    ["Prior therapy", "Distant metastases"],
    ["OS benefit", "Multiple concordant trials"],
    ["Older RT techniques", "Toxicity"],
    "Cisplatin-based chemoRT is standard.")

add("EMBRACE-I",
    ["Locally advanced cervical cancer", "MRI-guided brachytherapy"],
    ["Prior therapy", "Distant metastases"],
    ["Excellent local control", "Large prospective cohort"],
    ["Non-randomised", "Requires MRI access"],
    "MRI-guided brachytherapy is the gold standard.")

add("INTERLACE",
    ["Stage IB1 N+ to IVA cervical cancer", "Fit for chemotherapy"],
    ["Prior therapy", "Distant metastases"],
    ["OS benefit", "Low-cost regimen"],
    ["Few stage III–IVA patients", "Pre-IO era"],
    "Induction chemotherapy is a new option.")

add("KEYNOTE-A18",
    ["High-risk LACC", "FIGO 2014 IB2–IIB N+ or III–IVA"],
    ["Prior immunotherapy", "Active autoimmune disease"],
    ["OS benefit", "Double-blind"],
    ["Toxicity", "Cost"],
    "Pembrolizumab with chemoRT is a new standard.")

add("GOG 240",
    ["Recurrent/metastatic cervical cancer", "GOG PS 0–1"],
    ["Prior bevacizumab", "Fistula"],
    ["OS benefit", "Large trial"],
    ["Fistula risk", "Hypertension"],
    "Bevacizumab added to chemotherapy is standard.")

add("KEYNOTE-826",
    ["Persistent/recurrent/metastatic cervical cancer", "Not amenable to curative therapy"],
    ["Prior systemic therapy", "Active autoimmune disease"],
    ["OS benefit", "Double-blind"],
    ["Benefit mainly in PD-L1 positive", "Immune toxicity"],
    "Pembrolizumab with chemotherapy is first-line standard.")

add("SHAPE",
    ["Low-risk early cervical cancer (≤2 cm)", "Stromal invasion <10 mm"],
    ["High-risk features", "Lymph node metastases"],
    ["Non-inferior pelvic recurrence", "Less morbidity"],
    ["Low-risk patients only", "Requires precise imaging"],
    "Simple hysterectomy is standard for low-risk disease.")

add("LACC",
    ["Stage IA1–IB1 cervical cancer", "Fit for radical hysterectomy"],
    ["Prior therapy", "Lymph node metastases"],
    ["Showed worse OS with MIS", "Practice-changing"],
    ["Surgeon experience variable", "Uterine manipulator use"],
    "Open radical hysterectomy is standard.")

add("MARCH",
    ["Randomised trials of altered fractionation vs conventional RT in HNSCC", "Individual patient data"],
    ["Trials with concurrent chemotherapy in both arms", "Nasopharyngeal carcinoma"],
    ["Showed hyperfractionation gives the largest OS benefit (~8% at 5 years)", "Individual patient data"],
    ["Mostly RT-alone comparisons, pre-dating concurrent chemoRT", "Benefit smaller in older patients"],
    "Altered fractionation is an alternative when chemotherapy is not possible; with concurrent chemotherapy its added value is limited.")

add("JCOG1008",
    ["Postoperative high-risk HNSCC (positive margins or ECE)", "Fit for cisplatin"],
    ["Distant metastases", "Poor renal function"],
    ["Non-inferior OS with weekly 40 mg/m²", "Less toxicity"],
    ["Japanese population", "Locoregional control slightly worse in weekly arm"],
    "Weekly cisplatin 40 mg/m² is an acceptable alternative postoperatively, with Noronha suggesting caution.")

add("PARSPORT",
    ["Pharyngeal SCC (oropharynx, hypopharynx)", "T1–4, N0–3, M0"],
    ["Prior head and neck RT", "Distant metastases"],
    ["Randomised evidence that parotid-sparing IMRT reduces xerostomia", "Quality-of-life benefit"],
    ["Small trial (n=94)", "No survival endpoint"],
    "IMRT is standard for head and neck RT.")

add("TAX 324 / TAX 323",
    ["Locally advanced unresectable HNSCC (TAX 323) or resectable/unresectable (TAX 324)", "WHO PS 0–1"],
    ["Distant metastases", "Prior chemotherapy"],
    ["Showed TPF superior to PF induction", "OS benefit"],
    ["Did not compare induction with concurrent chemoRT alone", "Toxicity"],
    "TPF is the preferred induction regimen, but induction itself has not shown OS benefit over chemoRT in most trials.")

add("Sun / Zhang NPC GP induction",
    ["Locoregionally advanced nasopharyngeal carcinoma (stage III–IVB)", "Endemic Chinese population"],
    ["Distant metastases", "Prior treatment"],
    ["OS benefit", "GP induction well tolerated"],
    ["Endemic population (EBV-related)", "Chinese centres only"],
    "GP induction followed by chemoRT is standard for locoregionally advanced NPC.")

add("KEYNOTE-048",
    ["Recurrent or metastatic HNSCC (oral cavity, oropharynx, hypopharynx, larynx)", "Not curable by local therapy", "ECOG PS 0–1"],
    ["Progression within 6 months of curative treatment", "Nasopharyngeal carcinoma"],
    ["OS benefit for pembrolizumab ± chemo", "PD-L1 CPS-based selection"],
    ["Pembrolizumab monotherapy not beneficial in CPS <1", "Cost"],
    "Pembrolizumab ± chemotherapy is first-line standard; CPS testing guides choice.")

add("CheckMate 141",
    ["Recurrent or metastatic HNSCC", "Progression within 6 months of platinum"],
    ["Active autoimmune disease", "Untreated CNS metastases"],
    ["OS benefit over investigator's choice", "Better quality of life"],
    ["Investigator's choice included weak agents", "Low response rate (~13%)"],
    "Nivolumab is standard second-line therapy after platinum.")

add("Patil (Tata) metronomic",
    ["Recurrent or metastatic HNSCC", "Resource-limited setting", "ECOG PS 0–1"],
    ["Prior immunotherapy", "Active autoimmune disease"],
    ["Low-cost, low-dose nivolumab improved OS", "Pragmatic Indian trial"],
    ["Single-centre Indian trial", "Low-dose nivolumab not compared with full dose"],
    "Supports low-dose nivolumab as an affordable option in India.")

add("KEYNOTE-689",
    ["Resectable stage III–IVA HNSCC (oral cavity, larynx, hypopharynx, HPV-negative oropharynx)"],
    ["Distant metastases", "Prior immunotherapy"],
    ["EFS benefit with perioperative pembrolizumab", "No delay in surgery"],
    ["OS immature", "Benefit mainly in PD-L1 positive"],
    "Perioperative pembrolizumab is a new option for resectable HNSCC.")
