# Depth pass: leukaemia, melanoma/skin, sarcoma, RT, supportive care.
A = {}
def add(name, inc, exc, pros, cons, critique):
    A[name] = {"inclusion": inc, "exclusion": exc, "strengths": pros, "limitations": cons, "critique": critique}

add("Daunorubicin 90 vs 45 (E1900)",
    ["AML age <60", "Untreated"],
    ["Prior therapy", "APL"],
    ["OS benefit", "Large trial"],
    ["Benefit limited to younger patients", "Cardiotoxicity"],
    "Daunorubicin 90 mg/m² is standard; 60 mg/m² may be equivalent per UK NCRI AML17.")

add("RATIFY",
    ["FLT3-mutated AML age <60", "Untreated"],
    ["Prior therapy", "APL"],
    ["OS benefit", "Double-blind"],
    ["Many proceeded to transplant", "Rash"],
    "Midostaurin is standard for FLT3-mutated AML.")

add("VIALE-A",
    ["AML unfit for intensive chemo", "Age ≥75 or comorbidities"],
    ["Prior HMA", "Favourable-risk cytogenetics"],
    ["OS benefit", "High response rates"],
    ["Myelosuppression", "Infection risk"],
    "Ven-aza is standard for unfit AML.")

add("APL0406 (Lo-Coco)",
    ["Low/intermediate-risk APL", "WBC ≤10 × 10⁹/L"],
    ["High-risk APL", "QTc prolongation"],
    ["Superior EFS with ATRA + ATO", "Chemo-free"],
    ["Low-risk only", "QTc monitoring needed"],
    "ATRA + ATO is standard.")

add("IRIS",
    ["Chronic-phase CML", "Untreated"],
    ["Prior therapy", "Accelerated phase"],
    ["Dramatic outcomes improvement", "Long-term follow-up"],
    ["Crossover", "Cost"],
    "Imatinib transformed CML.")

add("PhALLCON / GIMEMA LAL2116",
    ["Ph+ ALL", "Untreated"],
    ["Prior therapy", "CNS involvement"],
    ["High MRD negativity", "Chemo-light approaches"],
    ["Toxicity", "OS immature"],
    "Chemo-free approaches are emerging.")

add("E1910",
    ["MRD-negative Ph-negative B-ALL age 30–70", "Complete remission"],
    ["Prior blinatumomab", "CNS involvement"],
    ["OS benefit", "Practice-changing"],
    ["Neurotoxicity", "Cost"],
    "Blinatumomab consolidation is standard.")

add("CheckMate 067",
    ["Untreated advanced melanoma", "ECOG PS 0–1"],
    ["Prior therapy", "Active brain metastases"],
    ["Durable OS benefit", "Long-term follow-up"],
    ["Toxicity", "Not powered for combo vs nivo"],
    "Nivo-ipi gives the longest survival but at high toxicity.")

add("RELATIVITY-047",
    ["Untreated advanced melanoma", "ECOG PS 0–1"],
    ["Prior therapy", "Active brain metastases"],
    ["PFS benefit", "Less toxicity than nivo-ipi"],
    ["OS not significant", "No comparison with nivo-ipi"],
    "Nivo-relatlimab is a less toxic alternative.")

add("COMBI-d/v & COLUMBUS",
    ["BRAF V600 melanoma", "Untreated"],
    ["Prior BRAF/MEK therapy", "Active brain metastases"],
    ["OS benefit", "Less skin toxicity than BRAFi alone"],
    ["Resistance develops", "Pyrexia (dabrafenib-trametinib)"],
    "BRAF/MEK combinations are standard.")

add("DREAMseq",
    ["BRAF V600 melanoma", "Untreated"],
    ["Prior therapy", "Active brain metastases"],
    ["Showed IO-first better", "Practice-changing"],
    ["Small trial", "Stopped early"],
    "Immunotherapy first is preferred.")

add("KEYNOTE-054 / CheckMate 238 / COMBI-AD",
    ["Resected stage III melanoma", "ECOG PS 0–1"],
    ["Prior therapy", "Uveal melanoma"],
    ["RFS benefit", "Three concordant trials"],
    ["OS not proven", "Toxicity"],
    "Adjuvant therapy is standard for stage III.")

add("SWOG S1801",
    ["Resectable stage III–IV melanoma", "ECOG PS 0–1"],
    ["Prior therapy", "Uveal melanoma"],
    ["EFS benefit", "Neoadjuvant strategy"],
    ["OS immature", "Small trial"],
    "Neoadjuvant pembrolizumab is preferred.")

add("NADINA",
    ["Macroscopic stage III melanoma", "Resectable"],
    ["Prior therapy", "Uveal melanoma"],
    ["EFS benefit", "Response-adapted surgery"],
    ["Toxicity", "OS immature"],
    "Neoadjuvant nivo-ipi is a new standard.")

add("MSLT-II / DeCOG-SLT",
    ["Melanoma with positive sentinel node", "Clinically node-negative"],
    ["Prior therapy", "Macroscopic nodal disease"],
    ["Showed no OS benefit for completion dissection", "Less lymphoedema"],
    ["Low-risk patients", "Ultrasound surveillance required"],
    "Completion dissection is no longer standard.")

add("mRNA-4157 + pembrolizumab (KEYNOTE-942)",
    ["Resected high-risk melanoma", "Stage III–IV"],
    ["Prior therapy", "Uveal melanoma"],
    ["RFS benefit", "Personalised approach"],
    ["Phase 2", "Small trial"],
    "Personalised vaccines are promising.")

add("Cemiplimab cSCC / Avelumab Merkel",
    ["Advanced cutaneous SCC / Merkel cell carcinoma", "Not amenable to surgery/RT"],
    ["Prior immunotherapy", "Organ transplant"],
    ["High response rates", "Durable responses"],
    ["Single-arm", "Immune toxicity"],
    "IO is standard for advanced cSCC and Merkel.")

add("ACOSOG Z9001 / SSG XVIII",
    ["Resected high-risk GIST", "KIT-positive"],
    ["Prior imatinib", "Distant metastases"],
    ["OS benefit with 3 years", "Long-term follow-up"],
    ["Optimal duration unclear", "Fatigue, oedema"],
    "3 years adjuvant imatinib is standard.")

add("B2222 / EORTC 62005",
    ["Advanced GIST", "KIT-positive"],
    ["Prior imatinib", "Poor organ function"],
    ["Defined imatinib efficacy", "Large trials"],
    ["Dose depends on KIT exon 9", "Resistance develops"],
    "Imatinib 400 mg is standard; 800 mg for exon 9.")

add("INVICTUS / VOYAGER",
    ["Advanced GIST after ≥3 TKIs (INVICTUS); PDGFRA D842V (NAVIGATOR)", "ECOG PS 0–2"],
    ["Prior ripretinib", "Poor organ function"],
    ["OS benefit", "Well tolerated"],
    ["Late-line only", "Alopecia, hand-foot syndrome"],
    "Ripretinib is standard fourth-line.")

add("O'Sullivan NCIC SR2",
    ["Extremity soft tissue sarcoma", "Resectable"],
    ["Prior RT", "Distant metastases"],
    ["Showed preop RT less fibrosis", "Lower dose"],
    ["More wound complications", "Lower-limb tumours most affected"],
    "Preoperative RT is preferred.")

add("STRASS",
    ["Primary retroperitoneal sarcoma", "Resectable"],
    ["Prior RT", "Distant metastases"],
    ["Showed no benefit overall", "Randomised in rare disease"],
    ["Possible benefit in liposarcoma", "Underpowered"],
    "Preop RT is not routine for RPS.")

add("EORTC 62012",
    ["Advanced soft tissue sarcoma", "Age 18–60"],
    ["Prior chemotherapy", "Poor organ function"],
    ["Higher response with combination", "Large trial"],
    ["No OS benefit", "Toxicity"],
    "Doxorubicin alone is standard; combination for response.")

add("EURAMOS-1",
    ["Resectable osteosarcoma", "Age ≤40"],
    ["Prior therapy", "Distant metastases"],
    ["Showed no benefit for intensification", "Large international trial"],
    ["Toxicity", "Poor responders still do poorly"],
    "MAP remains standard.")

add("EURO EWING 2012 / rEECur",
    ["Newly diagnosed Ewing sarcoma", "Age ≥2"],
    ["Prior therapy", "Poor organ function"],
    ["OS benefit", "Shorter treatment"],
    ["Toxicity", "Interval compression requires G-CSF"],
    "VDC/IE is standard.")

add("Hartsell RTOG 97-14",
    ["Painful bone metastases (breast/prostate)", "KPS ≥40"],
    ["Prior RT to site", "Pathological fracture"],
    ["Equal pain relief", "Convenience"],
    ["Higher retreatment rate", "Older trial"],
    "8 Gy single fraction is standard.")

add("SC.24 (spine SBRT)",
    ["Painful spinal metastases", "≤3 consecutive segments"],
    ["Prior RT to site", "Spinal cord compression"],
    ["Higher complete pain response", "Randomised"],
    ["Fracture risk", "Requires SBRT technology"],
    "SBRT is an option for spine metastases.")

add("Patchell MSCC",
    ["Metastatic spinal cord compression", "Single area of compression"],
    ["Radiosensitive tumours", "Paraplegia >48 hours"],
    ["Improved ambulation", "Randomised"],
    ["Selected patients", "Small trial"],
    "Surgery + RT is preferred for selected MSCC.")

add("SCORAD III",
    ["MSCC not suitable for surgery", "Life expectancy >8 weeks"],
    ["Prior RT", "Radiosensitive tumours"],
    ["Non-inferior ambulation", "Convenience"],
    ["Short survival", "Non-inferiority margin"],
    "8 Gy single fraction is acceptable.")

add("ORIOLE / STOMP",
    ["Oligometastatic/oligorecurrent prostate cancer", "≤3 lesions"],
    ["Prior ADT", "Castration resistance"],
    ["Delayed ADT", "Randomised"],
    ["Small trials", "Short follow-up"],
    "MDT is an option for oligometastatic prostate cancer.")

add("Navari olanzapine CINV",
    ["Highly emetogenic chemotherapy", "Chemotherapy-naive"],
    ["Prior olanzapine", "Antipsychotic use"],
    ["Improved nausea control", "Low cost"],
    ["Sedation", "Single trial"],
    "Olanzapine is standard for HEC.")

add("Hokusai VTE Cancer / SELECT-D / Caravaggio",
    ["Cancer-associated VTE", "Active cancer"],
    ["High bleeding risk", "Severe renal impairment"],
    ["Non-inferior VTE recurrence", "Oral therapy"],
    ["Higher GI bleeding with some DOACs", "GI cancers at higher risk"],
    "DOACs are standard for cancer VTE.")

add("Denosumab vs zoledronic acid (Stopeck / Fizazi)",
    ["Bone metastases (breast, prostate)", "No prior bisphosphonate"],
    ["Prior bisphosphonate", "Osteonecrosis of jaw"],
    ["Fewer skeletal events", "No renal dose adjustment"],
    ["No OS benefit", "Hypocalcaemia"],
    "Denosumab is preferred.")

add("ABCSG-18 / Early Breast EBCTCG bisphosphonates",
    ["Postmenopausal early BC on AI", "Adjuvant setting"],
    ["Prior bisphosphonate", "Osteonecrosis of jaw"],
    ["Reduced fractures and recurrence", "Meta-analysis support"],
    ["Osteonecrosis risk", "Benefit limited to postmenopausal"],
    "Adjuvant bisphosphonates are standard for postmenopausal women.")
