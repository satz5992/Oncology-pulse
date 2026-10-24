# Critical appraisal for GU and gynaecologic trials. Revision aid; verify against the primary paper.
A = {}
def add(name, inc, exc, pros, cons, critique):
    A[name] = {"inclusion": inc, "exclusion": exc, "strengths": pros, "limitations": cons, "critique": critique}

# Prostate
add("PIVOT / ProtecT",
    ["Localised prostate cancer (ProtecT: PSA-detected, age 50–69)", "Fit for radical treatment"],
    ["Metastatic disease", "Life expectancy <10 years"],
    ["ProtecT: population-based, 15-year follow-up, patient-reported outcomes", "Three-way comparison including active monitoring"],
    ["Mostly low-risk disease; monitoring less rigorous than modern active surveillance (no MRI)", "PIVOT older, underpowered"],
    "No prostate cancer mortality difference at 15 years, but more progression and metastasis with monitoring. Each treatment has a distinct toxicity profile, making shared decisions essential.")

add("RTOG 94-08",
    ["Localised prostate cancer T1b–T2b, PSA ≤20", "Low and intermediate risk"],
    ["High-risk features", "Prior hormonal therapy"],
    ["OS benefit for short-term ADT with RT"],
    ["RT dose 66.6 Gy — below modern dose-escalated standards", "Benefit confined to intermediate risk"],
    "Short-course ADT benefits intermediate-risk disease; with modern dose escalation the magnitude is debated.")

add("Bolla EORTC 22863",
    ["Locally advanced (T3–4) or high-grade T1–2 prostate cancer", "WHO PS 0–2"],
    ["Distant metastases"],
    ["OS benefit for long-term ADT with RT", "10-year follow-up"],
    ["Low RT dose (70 Gy)", "ADT side effects"],
    "Established long-term ADT with RT for high-risk disease.")

add("CHHiP",
    ["Localised prostate cancer T1b–T3a, N0", "PSA <30 ng/mL"],
    ["Prior pelvic RT", "Hip prosthesis"],
    ["Large non-inferiority trial", "Quality-assured IMRT"],
    ["Low proportion of high-risk patients"],
    "60 Gy/20 is standard moderate hypofractionation.")

add("HYPO-RT-PC / PACE-B",
    ["Low/intermediate-risk localised prostate cancer", "No ADT (PACE-B)"],
    ["High-risk disease", "Prior TURP (some)"],
    ["Non-inferior biochemical control", "Short overall treatment"],
    ["Higher acute GU toxicity in HYPO-RT-PC"],
    "Ultra-hypofractionation (5 fractions) is a standard option for low-intermediate risk.")

add("ASCENDE-RT",
    ["Intermediate or high-risk localised prostate cancer"],
    ["Distant metastases"],
    ["Improved biochemical control with LDR boost"],
    ["Higher GU toxicity", "No OS benefit"],
    "Brachytherapy boost improves PSA control but at higher urinary toxicity cost.")

add("RADICALS-RT / RAVES / GETUG-AFU 17 (ARTISTIC)",
    ["After radical prostatectomy with adverse features (pT3/4, positive margins)", "Post-op PSA ≤0.2 ng/mL"],
    ["Pelvic nodal metastases (some)"],
    ["Meta-analysis showed early salvage equivalent to adjuvant RT", "Avoided overtreatment"],
    ["Few very high-risk patients (pN1, Gleason 8–10)"],
    "Early salvage RT is preferred; adjuvant RT for very high-risk features remains debated.")

add("STAMPEDE (arm H) M1 RT",
    ["Newly diagnosed metastatic hormone-sensitive prostate cancer"],
    ["Prior radical treatment"],
    ["OS benefit for low metastatic burden"],
    ["No benefit in high-burden disease", "Burden defined by CHAARTED criteria on conventional imaging"],
    "Prostate RT is standard for low-volume mHSPC.")

add("CHAARTED",
    ["Newly diagnosed mHSPC", "ECOG PS 0–2"],
    ["Prior chemotherapy"],
    ["OS benefit for high-volume disease"],
    ["No benefit in low-volume", "Toxicity"],
    "Docetaxel benefit is clear in high-volume disease.")

add("LATITUDE / STAMPEDE abiraterone",
    ["High-risk newly diagnosed mHSPC (LATITUDE)", "STAMPEDE: high-risk M0 or M1"],
    ["Prior hormonal therapy"],
    ["Large OS benefit"],
    ["Mineralocorticoid side effects (hypertension, hypokalaemia)"],
    "Abiraterone is a standard addition to ADT; low-cost generics make it accessible in India.")

add("TITAN / ENZAMET / ARCHES",
    ["mHSPC", "ECOG PS 0–1"],
    ["Prior ARPI"],
    ["OS benefit across volumes"],
    ["Fatigue and falls"],
    "ARPIs with ADT are standard regardless of volume.")

add("PEACE-1 / ARASENS",
    ["De novo mHSPC", "Fit for docetaxel"],
    ["Prior ARPI"],
    ["OS benefit for triplet therapy"],
    ["Toxicity", "Doublet ARPI comparison lacking"],
    "Triplet therapy is an option for high-volume de novo disease.")

add("SPARTAN / PROSPER / ARAMIS",
    ["nmCRPC with PSA doubling time ≤10 months", "Conventional imaging negative for metastases"],
    ["Metastases on conventional imaging"],
    ["Metastasis-free and OS benefit"],
    ["PSMA-PET would reclassify many patients as metastatic"],
    "ARPIs are standard for high-risk nmCRPC, though PSMA-PET changes definitions.")

add("EMBARK",
    ["High-risk biochemical recurrence with PSADT ≤9 months", "No metastases on conventional imaging"],
    ["Prior hormonal therapy"],
    ["Metastasis-free survival benefit"],
    ["OS immature", "PSMA-PET not used"],
    "Enzalutamide + leuprolide is an option for high-risk BCR.")

add("TAX 327",
    ["mCRPC", "KPS ≥60"],
    ["Prior chemotherapy"],
    ["OS benefit"],
    ["Modest gain"],
    "Docetaxel became first chemotherapy to improve OS in mCRPC.")

add("COU-AA-301/302, AFFIRM, PREVAIL",
    ["mCRPC pre- or post-docetaxel"],
    ["Prior ARPI"],
    ["OS benefit"],
    ["Cross-resistance between ARPIs"],
    "ARPIs are standard; sequencing two ARPIs is less effective.")

add("TROPIC / CARD",
    ["mCRPC after docetaxel (and an ARPI in CARD)"],
    ["Prior cabazitaxel"],
    ["OS benefit"],
    ["Neutropenia"],
    "Cabazitaxel is preferred over a second ARPI after docetaxel and one ARPI.")

add("ALSYMPCA",
    ["Symptomatic bone-metastatic CRPC, ≥2 bone metastases", "No visceral metastases"],
    ["Visceral metastases", "Bulky nodes >3 cm"],
    ["OS benefit"],
    ["Pre-ARPI era"],
    "Radium-223 is an option for bone-only disease.")

add("VISION",
    ["PSMA-PET positive mCRPC", "After ARPI and taxane"],
    ["PSMA-negative lesions"],
    ["OS benefit"],
    ["Control arm excluded chemotherapy"],
    "Lu-PSMA is standard in later lines.")

add("PSMAfore",
    ["Taxane-naive PSMA+ mCRPC after one ARPI"],
    ["Prior taxane"],
    ["rPFS benefit"],
    ["OS confounded by crossover"],
    "Lu-PSMA is an option before docetaxel.")

add("PROfound",
    ["mCRPC with HRR alterations after ARPI"],
    ["Prior PARP inhibitor"],
    ["OS benefit in BRCA1/2, ATM cohort"],
    ["Benefit driven by BRCA"],
    "Olaparib is standard for BRCA-mutated mCRPC.")

add("TALAPRO-2 / PROpel",
    ["First-line mCRPC"],
    ["Prior ARPI in mCRPC"],
    ["rPFS benefit", "Benefit in HRR-mutated"],
    ["Limited benefit in HRR-negative"],
    "PARPi + ARPI is best for HRR-altered patients.")

# Bladder & upper tract
add("SWOG 8710",
    ["MIBC T2–T4a"],
    ["Distant metastases"],
    ["OS benefit"],
    ["Toxicity"],
    "Established neoadjuvant cisplatin-based chemo.")

add("VESPER",
    ["MIBC, cisplatin-eligible"],
    ["Distant metastases"],
    ["Improved PFS with ddMVAC"],
    ["Toxicity"],
    "ddMVAC is a preferred neoadjuvant option.")

add("NIAGARA",
    ["Cisplatin-eligible MIBC"],
    ["Prior immunotherapy"],
    ["EFS and OS benefit"],
    ["Contribution of adjuvant phase unclear"],
    "Perioperative durvalumab is a new standard.")

add("CheckMate 274",
    ["High-risk MIUC after radical surgery"],
    ["Prior immunotherapy"],
    ["DFS benefit"],
    ["OS data immature"],
    "Adjuvant nivolumab is standard for high-risk resected MIUC.")

add("BC2001",
    ["MIBC T2–T4a"],
    ["Distant metastases"],
    ["Improved locoregional control"],
    ["No OS benefit"],
    "Chemoradiotherapy with 5-FU/MMC is standard for bladder preservation.")

add("POUT",
    ["Upper-tract urothelial carcinoma pT2–T4 or N+"],
    ["Distant metastases"],
    ["DFS benefit"],
    ["OS benefit not significant"],
    "Adjuvant chemotherapy is standard for UTUC.")

add("JAVELIN Bladder 100",
    ["Advanced UC without progression after first-line platinum"],
    ["Prior immunotherapy"],
    ["OS benefit"],
    ["Pre-EV/pembro era"],
    "Avelumab maintenance remains an option after platinum.")

add("EV-302",
    ["Untreated advanced urothelial carcinoma"],
    ["Prior systemic therapy"],
    ["Large OS benefit"],
    ["Toxicity (rash, neuropathy, hyperglycaemia)"],
    "EV-pembro is the new first-line standard.")

add("CheckMate 901 (gem-cis + nivo)",
    ["Cisplatin-eligible advanced UC"],
    ["Prior systemic therapy"],
    ["OS benefit"],
    ["Superseded by EV-302"],
    "Nivo-gem-cis is an option for cisplatin-eligible patients.")

add("THOR",
    ["FGFR-altered advanced UC after ARPI/IO"],
    ["Prior FGFR inhibitor"],
    ["OS benefit"],
    ["Hyperphosphataemia and eye toxicity"],
    "Erdafitinib is standard for FGFR-altered UC.")

# Kidney
add("CheckMate 214",
    ["Advanced clear-cell RCC", "Treatment-naive"],
    ["Brain metastases"],
    ["Durable OS benefit in intermediate/poor risk"],
    ["Immune toxicity"],
    "Nivo-ipi is a standard first-line option.")

add("KEYNOTE-426 / CLEAR / CheckMate 9ER",
    ["Advanced ccRCC", "Treatment-naive"],
    ["Brain metastases"],
    ["OS benefit"],
    ["Toxicity of TKIs"],
    "IO-TKI combinations are standard.")

add("KEYNOTE-564",
    ["High-risk ccRCC after nephrectomy"],
    ["Distant metastases"],
    ["DFS and OS benefit"],
    ["Toxicity"],
    "Adjuvant pembrolizumab is standard.")

add("CARMENA",
    ["Synchronous mRCC, intermediate/poor risk"],
    ["Prior systemic therapy"],
    ["Showed sunitinib alone non-inferior"],
    ["Poor accrual", "High-risk patients"],
    "Cytoreductive nephrectomy is not mandatory in intermediate/poor risk.")

add("LITESPARK-005",
    ["Advanced ccRCC after IO and VEGF-TKI"],
    ["Prior HIF-2α inhibitor"],
    ["PFS benefit"],
    ["OS not significant"],
    "Belzutifan is an option in later lines.")

# Testis
add("Einhorn PVB / BEP (Williams)",
    ["Disseminated germ cell tumours"],
    ["Prior chemotherapy"],
    ["Reduced toxicity with BEP"],
    ["Older trial"],
    "BEP is standard for germ cell tumours.")

add("IGCCCG",
    ["Metastatic GCT"],
    ["None"],
    ["Defined prognostic groups"],
    ["Retrospective"],
    "Defines risk-adapted therapy.")

add("MRC TE19 (Oliver)",
    ["Stage I seminoma after orchidectomy"],
    ["Prior therapy"],
    ["Single-dose carboplatin non-inferior"],
    ["Surveillance now preferred"],
    "Carboplatin is an option; surveillance preferred for low-risk.")

# Gynaecologic
add("GOG 111 / OV-10",
    ["Stage III–IV ovarian cancer"],
    ["Prior chemotherapy"],
    ["OS benefit"],
    ["Cisplatin toxicity"],
    "Established platinum-paclitaxel as standard.")

add("GOG 172 (Armstrong IP)",
    ["Optimally debulked stage III ovarian cancer"],
    ["Prior chemotherapy"],
    ["OS benefit"],
    ["Toxicity and catheter complications"],
    "IP chemotherapy improves OS but is rarely used.")

add("JGOG 3016",
    ["Stage II–IV ovarian cancer"],
    ["Prior chemotherapy"],
    ["OS benefit with dose-dense"],
    ["Not replicated in Western trials"],
    "Dose-dense paclitaxel is an option, mainly in Asian patients.")

add("EORTC 55971 / CHORUS",
    ["Stage IIIC–IV ovarian cancer"],
    ["Prior therapy"],
    ["Non-inferior OS with NACT"],
    ["Low complete resection rates"],
    "NACT is acceptable for high tumour burden.")

add("OVHIPEC-1",
    ["Stage III ovarian cancer after NACT"],
    ["Prior HIPEC"],
    ["OS benefit"],
    ["Open-label", "Small trial"],
    "HIPEC at interval debulking is an option in experienced centres.")

add("SOLO-1",
    ["BRCA-mutated advanced ovarian cancer responding to platinum"],
    ["Prior PARP inhibitor"],
    ["Large PFS and OS benefit"],
    ["Limited to BRCA-mutated"],
    "Olaparib maintenance is standard for BRCA-mutated.")

add("PAOLA-1",
    ["Advanced ovarian cancer after platinum + bevacizumab"],
    ["Prior PARP inhibitor"],
    ["PFS and OS benefit in HRD-positive"],
    ["Little benefit in HRD-negative"],
    "Olaparib + bevacizumab is standard for HRD-positive.")

add("PRIMA",
    ["Advanced ovarian cancer responding to first-line platinum"],
    ["Prior PARP inhibitor"],
    ["PFS benefit"],
    ["No OS benefit"],
    "Niraparib is an option across biomarker groups.")

add("ICON7 / GOG 218",
    ["Advanced ovarian cancer"],
    ["Prior therapy"],
    ["PFS benefit"],
    ["OS benefit only in high-risk subgroup"],
    "Bevacizumab is an option for high-risk disease.")

add("MIRASOL",
    ["FRα-high platinum-resistant ovarian cancer"],
    ["Prior mirvetuximab"],
    ["OS benefit"],
    ["Ocular toxicity"],
    "Mirvetuximab is standard for FRα-high PROC.")

add("PORTEC-1/2",
    ["Intermediate/high-intermediate-risk endometrial cancer"],
    ["High-risk features"],
    ["Reduced local recurrence"],
    ["No OS benefit"],
    "Vaginal brachytherapy is standard for HIR.")

add("PORTEC-3",
    ["High-risk endometrial cancer"],
    ["Prior therapy"],
    ["Improved OS"],
    ["Toxicity"],
    "ChemoRT is standard for high-risk endometrial cancer.")

add("GOG 258",
    ["Stage III–IVA endometrial cancer"],
    ["Prior therapy"],
    ["No OS benefit for chemoRT"],
    ["Locoregional benefit"],
    "Chemotherapy alone is standard; chemoRT improves local control.")

add("RUBY / NRG-GY018",
    ["Stage III–IV or recurrent endometrial cancer"],
    ["Prior immunotherapy"],
    ["PFS benefit, OS in dMMR"],
    ["Limited benefit in pMMR"],
    "Chemo-IO is standard, especially for dMMR.")

add("KEYNOTE-775",
    ["Advanced endometrial cancer after platinum"],
    ["Prior lenvatinib"],
    ["OS benefit"],
    ["Toxicity"],
    "Lenvatinib-pembrolizumab is second-line standard.")

add("Cervix chemoRT (Rose / Morris, 1999 NCI alert)",
    ["Locally advanced cervical cancer"],
    ["Prior therapy"],
    ["OS benefit"],
    ["Older RT techniques"],
    "Cisplatin-based chemoRT is standard.")

add("EMBRACE-I",
    ["Locally advanced cervical cancer"],
    ["Prior therapy"],
    ["Excellent local control"],
    ["Non-randomised"],
    "MRI-guided brachytherapy is the gold standard.")

add("INTERLACE",
    ["Stage IB1 N+ to IVA cervical cancer"],
    ["Prior therapy"],
    ["OS benefit"],
    ["Few stage III–IVA patients"],
    "Induction chemotherapy is a new option.")

add("KEYNOTE-A18",
    ["High-risk LACC"],
    ["Prior immunotherapy"],
    ["OS benefit"],
    ["Toxicity"],
    "Pembrolizumab with chemoRT is a new standard.")

add("GOG 240",
    ["Recurrent/metastatic cervical cancer"],
    ["Prior bevacizumab"],
    ["OS benefit"],
    ["Fistula risk"],
    "Bevacizumab added to chemotherapy is standard.")

add("KEYNOTE-826",
    ["Persistent/recurrent/metastatic cervical cancer"],
    ["Prior systemic therapy"],
    ["OS benefit"],
    ["Benefit mainly in PD-L1 positive"],
    "Pembrolizumab with chemotherapy is first-line standard.")

add("SHAPE",
    ["Low-risk early cervical cancer (≤2 cm)"],
    ["High-risk features"],
    ["Non-inferior pelvic recurrence"],
    ["Low-risk patients only"],
    "Simple hysterectomy is standard for low-risk disease.")

add("LACC",
    ["Stage IA1–IB1 cervical cancer"],
    ["Prior therapy"],
    ["Showed worse OS with MIS"],
    ["Surgeon experience variable"],
    "Open radical hysterectomy is standard.")
