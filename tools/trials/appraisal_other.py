# Critical appraisal: head & neck, CNS, haematology, skin, sarcoma, RT, supportive care.
# Revision aid; verify against the primary paper.
A = {}
def add(name, inc, exc, pros, cons, critique):
    A[name] = {"inclusion": inc, "exclusion": exc, "strengths": pros, "limitations": cons, "critique": critique}

# Head & neck
add("MACH-NC",
    ["Randomised trials adding chemotherapy to locoregional treatment of non-metastatic HNSCC", "Individual patient data (>100 trials, ~19,000 patients)"],
    ["Nasopharyngeal carcinoma (analysed separately)", "Non-randomised data"],
    ["Individual patient data meta-analysis", "Showed timing matters: concurrent chemo gives ~6.5% 5-year OS gain"],
    ["Benefit declines with age; little or none >70 years", "Heterogeneous regimens and RT techniques", "Induction chemotherapy benefit not significant"],
    "Basis for concurrent chemoRT in HNSCC. The age interaction is important — elderly patients get little benefit and more toxicity.")

add("MARCH",
    ["Randomised trials of altered fractionation vs conventional RT in HNSCC", "Individual patient data"],
    ["Trials with concurrent chemotherapy in both arms (limited)"],
    ["Showed hyperfractionation gives the largest OS benefit (~8% at 5 years)"],
    ["Mostly RT-alone comparisons, pre-dating concurrent chemoRT", "Benefit smaller in older patients"],
    "Altered fractionation is an alternative when chemotherapy is not possible; with concurrent chemotherapy its added value is limited.")

add("RTOG 9501 / EORTC 22931",
    ["Resected HNSCC (oral cavity, oropharynx, larynx, hypopharynx)", "High-risk features: positive margins, extracapsular extension, ≥2 nodes (RTOG), or other adverse features (EORTC)", "Fit for cisplatin"],
    ["Distant metastases", "Prior RT to head and neck"],
    ["Two complementary randomised trials", "Pooled analysis identified margins and ECE as key indications"],
    ["High acute toxicity with 3-weekly cisplatin", "OS benefit in RTOG trial not significant in long-term follow-up overall"],
    "Postoperative chemoRT is standard for positive margins and ECE. Other risk factors gain less from chemotherapy.")

add("Bonner cetuximab-RT",
    ["Stage III–IV non-metastatic HNSCC of oropharynx, larynx or hypopharynx", "KPS ≥60"],
    ["Oral cavity primary", "Prior chemotherapy or RT"],
    ["OS benefit over RT alone", "Less mucositis than expected with cetuximab"],
    ["Compared with RT alone, not chemoRT", "Benefit largest in oropharynx (likely HPV-positive)"],
    "Cetuximab-RT is inferior to cisplatin-RT (RTOG 1016, De-ESCALaTE) and is now reserved for cisplatin-ineligible patients, where even its role is questioned.")

add("RTOG 1016 / De-ESCALaTE",
    ["HPV-positive (p16+) oropharyngeal SCC", "T1–T2 N2a–N3 or T3–T4 N0–N3 (RTOG 1016); low-risk (De-ESCALaTE)"],
    ["Distant metastases", "Prior head and neck RT"],
    ["Definitive de-escalation test", "Showed cisplatin superior to cetuximab"],
    ["Cetuximab arm not less toxic", "Excluded many cisplatin-ineligible patients"],
    "Cisplatin remains standard for HPV-positive oropharyngeal cancer. Cetuximab de-escalation failed; other de-escalation strategies are under study.")

add("Noronha (Tata) weekly vs 3-weekly cisplatin",
    ["Locally advanced HNSCC treated with chemoRT", "Mostly postoperative oral cavity cancer", "Indian population"],
    ["Distant metastases", "Poor renal function"],
    ["Pragmatic Indian trial", "Showed 3-weekly superior for locoregional control"],
    ["Mostly postoperative setting", "Weekly dose 30 mg/m² lower than many use (40 mg/m²)"],
    "Supports 3-weekly cisplatin in the postoperative setting. Many argue weekly 40 mg/m² (as in JCOG1008) is a fairer comparison.")

add("JCOG1008",
    ["Postoperative high-risk HNSCC (positive margins or ECE)", "Fit for cisplatin"],
    ["Distant metastases"],
    ["Non-inferior OS with weekly 40 mg/m²", "Less toxicity"],
    ["Japanese population", "Locoregional control slightly worse in weekly arm"],
    "Weekly cisplatin 40 mg/m² is an acceptable alternative postoperatively, with Noronha suggesting caution.")

add("PARSPORT",
    ["Pharyngeal SCC (oropharynx, hypopharynx)", "T1–4, N0–3, M0"],
    ["Prior head and neck RT"],
    ["Randomised evidence that parotid-sparing IMRT reduces xerostomia"],
    ["Small trial (n=94)"],
    "IMRT is standard for head and neck RT.")

add("VA Larynx / RTOG 91-11",
    ["Stage III–IV laryngeal SCC requiring total laryngectomy", "Fit for chemotherapy"],
    ["T4 with extensive cartilage invasion (RTOG 91-11)", "Distant metastases"],
    ["Established larynx preservation", "Long-term follow-up"],
    ["Late deaths unrelated to cancer higher in concurrent arm (RTOG 91-11)", "Excluded large T4 tumours"],
    "Concurrent cisplatin-RT gives the best larynx preservation, but late toxicity and non-cancer deaths are concerns.")

add("TAX 324 / TAX 323",
    ["Locally advanced unresectable HNSCC (TAX 323) or resectable/unresectable (TAX 324)", "WHO PS 0–1"],
    ["Distant metastases", "Prior chemotherapy"],
    ["Showed TPF superior to PF induction"],
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
    ["Active autoimmune disease"],
    ["OS benefit over investigator's choice"],
    ["Investigator's choice included weak agents"],
    "Nivolumab is standard second-line therapy after platinum.")

add("Patil (Tata) metronomic",
    ["Recurrent or metastatic HNSCC", "Resource-limited setting", "ECOG PS 0–1"],
    ["Prior immunotherapy"],
    ["Low-cost, low-dose nivolumab improved OS"],
    ["Single-centre Indian trial", "Low-dose nivolumab not compared with full dose"],
    "Supports low-dose nivolumab as an affordable option in India.")

add("KEYNOTE-689",
    ["Resectable stage III–IVA HNSCC (oral cavity, larynx, hypopharynx, HPV-negative oropharynx)"],
    ["Distant metastases", "Prior immunotherapy"],
    ["EFS benefit with perioperative pembrolizumab"],
    ["OS immature", "Benefit mainly in PD-L1 positive"],
    "Perioperative pembrolizumab is a new option for resectable HNSCC.")

# CNS
add("EORTC/NCIC (Stupp)",
    ["Newly diagnosed glioblastoma", "Age 18–70", "WHO PS 0–2"],
    ["Prior RT or chemotherapy"],
    ["OS benefit with long-term follow-up", "MGMT methylation identified as predictive"],
    ["Age ≤70 only", "Benefit small in unmethylated tumours"],
    "Established TMZ-RT as standard for GBM; MGMT status guides prognosis.")

add("Perry elderly GBM",
    ["Glioblastoma age ≥65", "ECOG PS 0–2"],
    ["Prior therapy"],
    ["OS benefit with TMZ in elderly"],
    ["Benefit greatest in MGMT-methylated"],
    "Short-course RT + TMZ is standard for elderly GBM.")

add("EF-14 (TTFields)",
    ["Newly diagnosed GBM after chemoRT", "KPS ≥70"],
    ["Prior TTFields"],
    ["OS benefit"],
    ["Open-label, no sham control", "Device burden and cost"],
    "TTFields improve OS, but the lack of a sham control and cost limit adoption.")

add("RTOG 9802 / EORTC 22033",
    ["High-risk low-grade glioma (age ≥40 or subtotal resection)"],
    ["Prior RT"],
    ["OS benefit with PCV"],
    ["Pre-molecular era"],
    "RT + PCV is standard for high-risk LGG.")

add("RTOG 9402 / EORTC 26951",
    ["Anaplastic oligodendroglial tumours"],
    ["Prior RT"],
    ["OS benefit in 1p/19q codeleted"],
    ["Pre-molecular era"],
    "RT + PCV is standard for codeleted oligodendroglioma.")

add("CATNON",
    ["1p/19q non-codeleted anaplastic glioma"],
    ["Prior RT"],
    ["OS benefit with adjuvant TMZ"],
    ["Benefit restricted to IDH-mutant"],
    "Adjuvant TMZ is standard for IDH-mutant astrocytoma.")

add("INDIGO",
    ["Residual or recurrent grade 2 IDH-mutant glioma after surgery only", "No prior RT or chemotherapy"],
    ["Prior RT or chemotherapy", "High-risk features needing immediate treatment"],
    ["PFS benefit and delayed need for further therapy"],
    ["OS not yet shown", "Cost"],
    "Vorasidenib can delay RT/chemo in selected low-grade gliomas.")

add("Patchell (surgery + WBRT)",
    ["Single brain metastasis", "KPS ≥70"],
    ["Multiple brain metastases"],
    ["OS benefit for surgery"],
    ["Small trial (n=48)"],
    "Surgery is standard for single, accessible brain metastasis.")

add("N0574 (Brown)",
    ["1–3 brain metastases"],
    ["Prior WBRT"],
    ["Less cognitive decline with SRS alone"],
    ["No OS difference"],
    "SRS alone is preferred for limited brain metastases.")

add("JLGK0901 (Yamamoto)",
    ["1–10 brain metastases (≤10 mL total)", "KPS ≥70"],
    ["Prior WBRT"],
    ["Non-inferior OS for 5–10 vs 2–4 metastases"],
    ["Observational"],
    "SRS is an option for up to 10 brain metastases.")

add("NRG CC001",
    ["Brain metastases for WBRT"],
    ["Prior WBRT"],
    ["Less cognitive decline with hippocampal avoidance"],
    ["No OS benefit"],
    "HA-WBRT + memantine is standard when WBRT is used.")

add("QUARTZ",
    ["NSCLC brain metastases unsuitable for surgery/SRS"],
    ["Prior WBRT"],
    ["Showed no OS benefit from WBRT"],
    ["Poor prognosis patients"],
    "WBRT can be omitted in poor-prognosis patients.")

# Myeloma
add("IFM 2009",
    ["Newly diagnosed myeloma age ≤65"],
    ["Prior therapy"],
    ["PFS benefit with early ASCT"],
    ["No OS benefit"],
    "Early ASCT remains standard; deferral is an option.")

add("GRIFFIN / PERSEUS",
    ["Transplant-eligible NDMM"],
    ["Prior therapy"],
    ["PFS benefit and MRD negativity"],
    ["OS immature"],
    "D-VRd is the new standard induction.")

add("MAIA",
    ["Transplant-ineligible NDMM"],
    ["Prior therapy"],
    ["PFS and OS benefit"],
    ["Continuous therapy"],
    "D-Rd is standard for transplant-ineligible patients.")

add("CEPHEUS / IMROZ",
    ["Transplant-ineligible/deferred NDMM"],
    ["Prior therapy"],
    ["PFS benefit"],
    ["Toxicity in elderly"],
    "Quadruplet therapy is an option for fit elderly.")

add("CALGB 100104 / Myeloma XI",
    ["Post-ASCT myeloma"],
    ["Prior lenalidomide"],
    ["OS benefit"],
    ["Second primary malignancies"],
    "Lenalidomide maintenance is standard.")

add("CARTITUDE-4",
    ["Lenalidomide-refractory MM, 1–3 prior lines"],
    ["Prior BCMA therapy"],
    ["PFS and OS benefit"],
    ["Early deaths, CRS and neurotoxicity"],
    "Cilta-cel is an option in early relapse; access is limited.")

add("MajesTEC-3",
    ["Relapsed/refractory MM, 1–3 prior lines"],
    ["Prior BCMA therapy"],
    ["PFS and OS benefit"],
    ["Infection risk"],
    "Teclistamab + daratumumab is a new option.")

# Lymphoma
add("GELA LNH98-5 (R-CHOP)",
    ["DLBCL age 60–80"],
    ["Prior therapy"],
    ["OS benefit"],
    ["Elderly only"],
    "R-CHOP became standard for DLBCL.")

add("POLARIX",
    ["Intermediate/high-risk DLBCL (IPI 2–5)"],
    ["Prior therapy"],
    ["PFS benefit"],
    ["No OS benefit"],
    "Pola-R-CHP is an alternative to R-CHOP.")

add("ZUMA-7 / TRANSFORM",
    ["Primary refractory or early relapse LBCL"],
    ["Prior CAR-T"],
    ["EFS and OS benefit"],
    ["Access and cost"],
    "CAR-T is standard second-line for early relapse.")

add("HD10 / HD16 / RAPID",
    ["Early-stage favourable Hodgkin lymphoma"],
    ["Prior therapy"],
    ["Defined de-escalation"],
    ["PFS slightly worse without RT"],
    "PET-guided RT omission is an option, with slightly higher relapse.")

add("RATHL",
    ["Advanced Hodgkin lymphoma"],
    ["Prior therapy"],
    ["Showed bleomycin can be dropped"],
    ["PET-positive patients had poor outcomes"],
    "PET-adapted AVD is standard.")

add("ECHELON-1",
    ["Stage III–IV Hodgkin lymphoma"],
    ["Prior therapy"],
    ["OS benefit"],
    ["Neuropathy"],
    "A-AVD is an option for advanced HL.")

add("HD21",
    ["Advanced HL"],
    ["Prior therapy"],
    ["Superior PFS and less toxicity"],
    ["Intensive regimen"],
    "BrECADD is a new standard for fit patients.")

add("S1826",
    ["Stage III–IV HL, age ≥12"],
    ["Prior therapy"],
    ["PFS benefit"],
    ["OS immature"],
    "N-AVD is a new standard.")

add("PRIMA (FL)",
    ["Advanced FL responding to R-chemo"],
    ["Prior therapy"],
    ["PFS benefit"],
    ["No OS benefit"],
    "Rituximab maintenance is an option.")

add("StiL / BRIGHT",
    ["Indolent NHL and MCL"],
    ["Prior therapy"],
    ["PFS benefit and less toxicity"],
    ["Infection risk"],
    "BR is a standard first-line option.")

add("TRIANGLE",
    ["Younger fit MCL"],
    ["Prior therapy"],
    ["Showed ASCT may be omitted with ibrutinib"],
    ["OS immature"],
    "Ibrutinib-based therapy may replace ASCT.")

add("CLL14 / ELEVATE-TN / RESONATE-2",
    ["Untreated CLL"],
    ["Prior therapy"],
    ["PFS benefit"],
    ["Continuous vs fixed duration"],
    "Targeted agents are standard first-line therapy.")

# Leukaemia
add("Daunorubicin 90 vs 45 (E1900)",
    ["AML age <60"],
    ["Prior therapy"],
    ["OS benefit"],
    ["Benefit limited to younger patients"],
    "Daunorubicin 90 mg/m² is standard.")

add("RATIFY",
    ["FLT3-mutated AML age <60"],
    ["Prior therapy"],
    ["OS benefit"],
    ["Many proceeded to transplant"],
    "Midostaurin is standard for FLT3-mutated AML.")

add("VIALE-A",
    ["AML unfit for intensive chemo"],
    ["Prior therapy"],
    ["OS benefit"],
    ["Myelosuppression"],
    "Ven-aza is standard for unfit AML.")

add("APL0406 (Lo-Coco)",
    ["Low/intermediate-risk APL"],
    ["High-risk APL"],
    ["Superior EFS with ATRA + ATO"],
    ["Low-risk only"],
    "ATRA + ATO is standard.")

add("IRIS",
    ["Chronic-phase CML"],
    ["Prior therapy"],
    ["Dramatic outcomes improvement"],
    ["Crossover"],
    "Imatinib transformed CML.")

add("PhALLCON / GIMEMA LAL2116",
    ["Ph+ ALL"],
    ["Prior therapy"],
    ["High MRD negativity"],
    ["Toxicity"],
    "Chemo-free approaches are emerging.")

add("E1910",
    ["MRD-negative Ph-negative B-ALL age 30–70"],
    ["Prior therapy"],
    ["OS benefit"],
    ["Neurotoxicity"],
    "Blinatumomab consolidation is standard.")

# Melanoma & skin
add("CheckMate 067",
    ["Untreated advanced melanoma"],
    ["Prior therapy"],
    ["Durable OS benefit"],
    ["Toxicity"],
    "Nivo-ipi gives the longest survival but at high toxicity.")

add("RELATIVITY-047",
    ["Untreated advanced melanoma"],
    ["Prior therapy"],
    ["PFS benefit"],
    ["OS not significant"],
    "Nivo-relatlimab is a less toxic alternative.")

add("COMBI-d/v & COLUMBUS",
    ["BRAF V600 melanoma"],
    ["Prior BRAF/MEK therapy"],
    ["OS benefit"],
    ["Resistance develops"],
    "BRAF/MEK combinations are standard.")

add("DREAMseq",
    ["BRAF V600 melanoma"],
    ["Prior therapy"],
    ["Showed IO-first better"],
    ["Small trial"],
    "Immunotherapy first is preferred.")

add("KEYNOTE-054 / CheckMate 238 / COMBI-AD",
    ["Resected stage III melanoma"],
    ["Prior therapy"],
    ["RFS benefit"],
    ["OS not proven"],
    "Adjuvant therapy is standard for stage III.")

add("SWOG S1801",
    ["Resectable stage III–IV melanoma"],
    ["Prior therapy"],
    ["EFS benefit"],
    ["OS immature"],
    "Neoadjuvant pembrolizumab is preferred.")

add("NADINA",
    ["Macroscopic stage III melanoma"],
    ["Prior therapy"],
    ["EFS benefit"],
    ["Toxicity"],
    "Neoadjuvant nivo-ipi is a new standard.")

add("MSLT-II / DeCOG-SLT",
    ["Melanoma with positive sentinel node"],
    ["Prior therapy"],
    ["Showed no OS benefit for completion dissection"],
    ["Low-risk patients"],
    "Completion dissection is no longer standard.")

add("mRNA-4157 + pembrolizumab (KEYNOTE-942)",
    ["Resected high-risk melanoma"],
    ["Prior therapy"],
    ["RFS benefit"],
    ["Phase 2"],
    "Personalised vaccines are promising.")

add("Cemiplimab cSCC / Avelumab Merkel",
    ["Advanced cutaneous SCC / Merkel cell carcinoma"],
    ["Prior therapy"],
    ["High response rates"],
    ["Single-arm"],
    "IO is standard for advanced cSCC and Merkel.")

# Sarcoma & GIST
add("ACOSOG Z9001 / SSG XVIII",
    ["Resected high-risk GIST"],
    ["Prior therapy"],
    ["OS benefit with 3 years"],
    ["Optimal duration unclear"],
    "3 years adjuvant imatinib is standard.")

add("B2222 / EORTC 62005",
    ["Advanced GIST"],
    ["Prior therapy"],
    ["Defined imatinib efficacy"],
    ["Dose depends on KIT exon 9"],
    "Imatinib 400 mg is standard; 800 mg for exon 9.")

add("INVICTUS / VOYAGER",
    ["Advanced GIST after ≥3 TKIs (INVICTUS); PDGFRA D842V (NAVIGATOR)"],
    ["Prior ripretinib"],
    ["OS benefit"],
    ["Late-line only"],
    "Ripretinib is standard fourth-line.")

add("O'Sullivan NCIC SR2",
    ["Extremity soft tissue sarcoma"],
    ["Prior RT"],
    ["Showed preop RT less fibrosis"],
    ["More wound complications"],
    "Preoperative RT is preferred.")

add("STRASS",
    ["Primary retroperitoneal sarcoma"],
    ["Prior RT"],
    ["Showed no benefit overall"],
    ["Possible benefit in liposarcoma"],
    "Preop RT is not routine for RPS.")

add("EORTC 62012",
    ["Advanced soft tissue sarcoma"],
    ["Prior chemotherapy"],
    ["Higher response with combination"],
    ["No OS benefit"],
    "Doxorubicin alone is standard; combination for response.")

add("EURAMOS-1",
    ["Resectable osteosarcoma"],
    ["Prior therapy"],
    ["Showed no benefit for intensification"],
    ["Toxicity"],
    "MAP remains standard.")

add("EURO EWING 2012 / rEECur",
    ["Newly diagnosed Ewing sarcoma"],
    ["Prior therapy"],
    ["OS benefit"],
    ["Toxicity"],
    "VDC/IE is standard.")

# RT general
add("Hartsell RTOG 97-14",
    ["Painful bone metastases (breast/prostate)"],
    ["Prior RT"],
    ["Equal pain relief"],
    ["Higher retreatment rate"],
    "8 Gy single fraction is standard.")

add("SC.24 (spine SBRT)",
    ["Painful spinal metastases"],
    ["Prior RT"],
    ["Higher complete pain response"],
    ["Fracture risk"],
    "SBRT is an option for spine metastases.")

add("Patchell MSCC",
    ["Metastatic spinal cord compression"],
    ["Radiosensitive tumours"],
    ["Improved ambulation"],
    ["Selected patients"],
    "Surgery + RT is preferred for selected MSCC.")

add("SCORAD III",
    ["MSCC not suitable for surgery"],
    ["Prior RT"],
    ["Non-inferior ambulation"],
    ["Short survival"],
    "8 Gy single fraction is acceptable.")

add("ORIOLE / STOMP",
    ["Oligometastatic/oligorecurrent prostate cancer"],
    ["Prior therapy"],
    ["Delayed ADT"],
    ["Small trials"],
    "MDT is an option for oligometastatic prostate cancer.")

# Supportive care
add("Navari olanzapine CINV",
    ["Highly emetogenic chemotherapy"],
    ["Prior olanzapine"],
    ["Improved nausea control"],
    ["Sedation"],
    "Olanzapine is standard for HEC.")

add("Hokusai VTE Cancer / SELECT-D / Caravaggio",
    ["Cancer-associated VTE"],
    ["High bleeding risk"],
    ["Non-inferior VTE recurrence"],
    ["Higher GI bleeding with some DOACs"],
    "DOACs are standard for cancer VTE.")

add("Denosumab vs zoledronic acid (Stopeck / Fizazi)",
    ["Bone metastases (breast, prostate)"],
    ["Prior bisphosphonate"],
    ["Fewer skeletal events"],
    ["No OS benefit"],
    "Denosumab is preferred.")

add("ABCSG-18 / Early Breast EBCTCG bisphosphonates",
    ["Postmenopausal early BC on AI"],
    ["Prior bisphosphonate"],
    ["Reduced fractures and recurrence"],
    ["Osteonecrosis risk"],
    "Adjuvant bisphosphonates are standard for postmenopausal women.")
