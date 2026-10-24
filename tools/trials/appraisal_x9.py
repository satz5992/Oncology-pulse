# Depth pass: CNS, myeloma, lymphoma.
A = {}
def add(name, inc, exc, pros, cons, critique):
    A[name] = {"inclusion": inc, "exclusion": exc, "strengths": pros, "limitations": cons, "critique": critique}

add("KEYNOTE-689",
    ["Resectable stage III–IVA HNSCC (oral cavity, larynx, hypopharynx, HPV-negative oropharynx)", "ECOG PS 0–1"],
    ["Distant metastases", "Prior immunotherapy"],
    ["EFS benefit with perioperative pembrolizumab", "No delay in surgery"],
    ["OS immature", "Benefit mainly in PD-L1 positive"],
    "Perioperative pembrolizumab is a new option for resectable HNSCC.")

add("EORTC/NCIC (Stupp)",
    ["Newly diagnosed glioblastoma", "Age 18–70", "WHO PS 0–2"],
    ["Prior RT or chemotherapy", "Significant comorbidity"],
    ["OS benefit with long-term follow-up", "MGMT methylation identified as predictive"],
    ["Age ≤70 only", "Benefit small in unmethylated tumours"],
    "Established TMZ-RT as standard for GBM; MGMT status guides prognosis.")

add("Perry elderly GBM",
    ["Glioblastoma age ≥65", "ECOG PS 0–2"],
    ["Prior therapy", "Significant comorbidity"],
    ["OS benefit with TMZ in elderly", "Short-course RT"],
    ["Benefit greatest in MGMT-methylated", "Myelosuppression"],
    "Short-course RT + TMZ is standard for elderly GBM.")

add("EF-14 (TTFields)",
    ["Newly diagnosed GBM after chemoRT", "KPS ≥70"],
    ["Prior TTFields", "Infratentorial tumour"],
    ["OS benefit", "Long-term follow-up"],
    ["Open-label, no sham control", "Device burden and cost"],
    "TTFields improve OS, but the lack of a sham control and cost limit adoption.")

add("RTOG 9802 / EORTC 22033",
    ["High-risk low-grade glioma (age ≥40 or subtotal resection)", "KPS ≥60"],
    ["Prior RT", "Prior chemotherapy"],
    ["OS benefit with PCV", "Long-term follow-up"],
    ["Pre-molecular era", "PCV toxicity"],
    "RT + PCV is standard for high-risk LGG.")

add("RTOG 9402 / EORTC 26951",
    ["Anaplastic oligodendroglial tumours", "KPS ≥60"],
    ["Prior RT", "Prior chemotherapy"],
    ["OS benefit in 1p/19q codeleted", "Long-term follow-up"],
    ["Pre-molecular era", "PCV toxicity"],
    "RT + PCV is standard for codeleted oligodendroglioma.")

add("CATNON",
    ["1p/19q non-codeleted anaplastic glioma", "WHO PS 0–2"],
    ["Prior RT", "Prior chemotherapy"],
    ["OS benefit with adjuvant TMZ", "2×2 factorial design"],
    ["Benefit restricted to IDH-mutant", "No benefit for concurrent TMZ"],
    "Adjuvant TMZ is standard for IDH-mutant astrocytoma.")

add("INDIGO",
    ["Residual or recurrent grade 2 IDH-mutant glioma after surgery only", "No prior RT or chemotherapy"],
    ["Prior RT or chemotherapy", "High-risk features needing immediate treatment"],
    ["PFS benefit and delayed need for further therapy", "Oral therapy"],
    ["OS not yet shown", "Cost"],
    "Vorasidenib can delay RT/chemo in selected low-grade gliomas.")

add("Patchell (surgery + WBRT)",
    ["Single brain metastasis", "KPS ≥70"],
    ["Multiple brain metastases", "Radiosensitive tumours"],
    ["OS benefit for surgery", "Better functional independence"],
    ["Small trial (n=48)", "Pre-SRS era"],
    "Surgery is standard for single, accessible brain metastasis.")

add("N0574 (Brown)",
    ["1–3 brain metastases", "Each <3 cm"],
    ["Prior WBRT", "Leptomeningeal disease"],
    ["Less cognitive decline with SRS alone", "Cognitive endpoints"],
    ["No OS difference", "Higher intracranial recurrence without WBRT"],
    "SRS alone is preferred for limited brain metastases.")

add("JLGK0901 (Yamamoto)",
    ["1–10 brain metastases (≤10 mL total)", "KPS ≥70"],
    ["Prior WBRT", "Leptomeningeal disease"],
    ["Non-inferior OS for 5–10 vs 2–4 metastases", "Large prospective study"],
    ["Observational", "Japanese centres only"],
    "SRS is an option for up to 10 brain metastases.")

add("NRG CC001",
    ["Brain metastases for WBRT", "KPS ≥70"],
    ["Prior WBRT", "Metastases within 5 mm of hippocampus"],
    ["Less cognitive decline with hippocampal avoidance", "Quality-of-life benefit"],
    ["No OS benefit", "Requires IMRT"],
    "HA-WBRT + memantine is standard when WBRT is used.")

add("QUARTZ",
    ["NSCLC brain metastases unsuitable for surgery/SRS", "Poor prognosis"],
    ["Prior WBRT", "Good prognosis candidates for SRS"],
    ["Showed no OS benefit from WBRT", "Quality-of-life data"],
    ["Poor prognosis patients", "Pre-targeted therapy era"],
    "WBRT can be omitted in poor-prognosis patients.")

add("IFM 2009",
    ["Newly diagnosed myeloma age ≤65", "Transplant-eligible"],
    ["Prior therapy", "Significant comorbidity"],
    ["PFS benefit with early ASCT", "MRD data"],
    ["No OS benefit", "1 year lenalidomide maintenance only"],
    "Early ASCT remains standard; deferral is an option.")

add("GRIFFIN / PERSEUS",
    ["Transplant-eligible NDMM", "Age ≤70"],
    ["Prior therapy", "Significant comorbidity"],
    ["PFS benefit and MRD negativity", "Quadruplet induction"],
    ["OS immature", "Infection risk"],
    "D-VRd is the new standard induction.")

add("MAIA",
    ["Transplant-ineligible NDMM", "ECOG PS 0–2"],
    ["Prior therapy", "Significant comorbidity"],
    ["PFS and OS benefit", "Long-term follow-up"],
    ["Continuous therapy", "Infection risk"],
    "D-Rd is standard for transplant-ineligible patients.")

add("CEPHEUS / IMROZ",
    ["Transplant-ineligible/deferred NDMM", "Age ≤80 (IMROZ)"],
    ["Prior therapy", "Frail patients"],
    ["PFS benefit", "MRD negativity"],
    ["Toxicity in elderly", "Treatment-related deaths"],
    "Quadruplet therapy is an option for fit elderly.")

add("CALGB 100104 / Myeloma XI",
    ["Post-ASCT myeloma", "Responding disease"],
    ["Prior lenalidomide", "Progressive disease"],
    ["OS benefit", "Large trials"],
    ["Second primary malignancies", "Continuous therapy"],
    "Lenalidomide maintenance is standard.")

add("CARTITUDE-4",
    ["Lenalidomide-refractory MM, 1–3 prior lines", "ECOG PS 0–1"],
    ["Prior BCMA therapy", "CNS involvement"],
    ["PFS and OS benefit", "Single infusion"],
    ["Early deaths, CRS and neurotoxicity", "Access and cost"],
    "Cilta-cel is an option in early relapse; access is limited.")

add("MajesTEC-3",
    ["Relapsed/refractory MM, 1–3 prior lines", "ECOG PS 0–1"],
    ["Prior BCMA therapy", "CNS involvement"],
    ["PFS and OS benefit", "Off-the-shelf therapy"],
    ["Infection risk", "CRS"],
    "Teclistamab + daratumumab is a new option.")

add("GELA LNH98-5 (R-CHOP)",
    ["DLBCL age 60–80", "Untreated"],
    ["Prior therapy", "CNS involvement"],
    ["OS benefit", "Long-term follow-up"],
    ["Elderly only", "Rituximab cost"],
    "R-CHOP became standard for DLBCL.")

add("POLARIX",
    ["Intermediate/high-risk DLBCL (IPI 2–5)", "Untreated"],
    ["Prior therapy", "CNS involvement"],
    ["PFS benefit", "Similar toxicity"],
    ["No OS benefit", "Cost"],
    "Pola-R-CHP is an alternative to R-CHOP.")

add("ZUMA-7 / TRANSFORM",
    ["Primary refractory or early relapse LBCL", "Transplant-eligible"],
    ["Prior CAR-T", "CNS involvement"],
    ["EFS and OS benefit", "Practice-changing"],
    ["Access and cost", "CRS and neurotoxicity"],
    "CAR-T is standard second-line for early relapse.")

add("HD10 / HD16 / RAPID",
    ["Early-stage favourable Hodgkin lymphoma", "Untreated"],
    ["Prior therapy", "Unfavourable risk factors"],
    ["Defined de-escalation", "Long-term follow-up"],
    ["PFS slightly worse without RT", "PET interpretation"],
    "PET-guided RT omission is an option, with slightly higher relapse.")

add("RATHL",
    ["Advanced Hodgkin lymphoma", "Untreated"],
    ["Prior therapy", "Age >60 (some)"],
    ["Showed bleomycin can be dropped", "Less lung toxicity"],
    ["PET-positive patients had poor outcomes", "Non-inferiority margin"],
    "PET-adapted AVD is standard.")

add("ECHELON-1",
    ["Stage III–IV Hodgkin lymphoma", "Untreated"],
    ["Prior therapy", "Neuropathy"],
    ["OS benefit", "Removed bleomycin"],
    ["Neuropathy", "Febrile neutropenia"],
    "A-AVD is an option for advanced HL.")

add("HD21",
    ["Advanced HL", "Age 18–60"],
    ["Prior therapy", "Neuropathy"],
    ["Superior PFS and less toxicity", "Fertility preservation"],
    ["Intensive regimen", "Requires PET"],
    "BrECADD is a new standard for fit patients.")

add("S1826",
    ["Stage III–IV HL, age ≥12", "Untreated"],
    ["Prior therapy", "Active autoimmune disease"],
    ["PFS benefit", "Less toxicity"],
    ["OS immature", "Immune toxicity"],
    "N-AVD is a new standard.")

add("PRIMA (FL)",
    ["Advanced FL responding to R-chemo", "High tumour burden"],
    ["Prior therapy", "Transformation"],
    ["PFS benefit", "Long-term follow-up"],
    ["No OS benefit", "Infection risk"],
    "Rituximab maintenance is an option.")

add("StiL / BRIGHT",
    ["Indolent NHL and MCL", "Untreated"],
    ["Prior therapy", "Transformation"],
    ["PFS benefit and less toxicity", "No alopecia"],
    ["Infection risk", "Prolonged lymphopenia"],
    "BR is a standard first-line option.")

add("TRIANGLE",
    ["Younger fit MCL", "Untreated"],
    ["Prior therapy", "CNS involvement"],
    ["Showed ASCT may be omitted with ibrutinib", "FFS benefit"],
    ["OS immature", "Cardiac toxicity"],
    "Ibrutinib-based therapy may replace ASCT.")

add("CLL14 / ELEVATE-TN / RESONATE-2",
    ["Untreated CLL", "Comorbid or elderly"],
    ["Prior therapy", "Richter transformation"],
    ["PFS benefit", "Fixed duration option"],
    ["Continuous vs fixed duration", "Cardiac toxicity (BTKi)"],
    "Targeted agents are standard first-line therapy.")
