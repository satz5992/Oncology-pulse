# Depth pass: prostate, bladder, kidney, testis.
A = {}
def add(name, inc, exc, pros, cons, critique):
    A[name] = {"inclusion": inc, "exclusion": exc, "strengths": pros, "limitations": cons, "critique": critique}

add("CHHiP",
    ["Localised prostate cancer T1b–T3a, N0", "PSA <30 ng/mL", "Risk of seminal vesicle involvement <30%"],
    ["Prior pelvic RT", "Hip prosthesis"],
    ["Large non-inferiority trial (n=3,216)", "Quality-assured IMRT"],
    ["Low proportion of high-risk patients", "Most received short-course ADT"],
    "60 Gy/20 is standard moderate hypofractionation and saves 3 weeks of treatment.")

add("HYPO-RT-PC / PACE-B",
    ["Low/intermediate-risk localised prostate cancer", "No ADT (PACE-B)"],
    ["High-risk disease", "Prior TURP (some)"],
    ["Non-inferior biochemical control", "Short overall treatment (1–2 weeks)"],
    ["Higher acute GU toxicity in HYPO-RT-PC", "Low/intermediate-risk only"],
    "Ultra-hypofractionation (5 fractions) is a standard option for low-intermediate risk.")

add("ASCENDE-RT",
    ["Intermediate or high-risk localised prostate cancer", "All received 12 months ADT"],
    ["Distant metastases", "Prior TURP"],
    ["Improved biochemical control with LDR boost", "Long-term follow-up"],
    ["Higher GU toxicity", "No OS benefit"],
    "Brachytherapy boost improves PSA control but at higher urinary toxicity cost.")

add("RADICALS-RT / RAVES / GETUG-AFU 17 (ARTISTIC)",
    ["After radical prostatectomy with adverse features (pT3/4, positive margins)", "Post-op PSA ≤0.2 ng/mL"],
    ["Pelvic nodal metastases (some)", "Prior hormonal therapy"],
    ["Meta-analysis showed early salvage equivalent to adjuvant RT", "Avoided overtreatment in ~half"],
    ["Few very high-risk patients (pN1, Gleason 8–10)", "Low event rates"],
    "Early salvage RT is preferred; adjuvant RT for very high-risk features remains debated.")

add("STAMPEDE (arm H) M1 RT",
    ["Newly diagnosed metastatic hormone-sensitive prostate cancer", "WHO PS 0–2"],
    ["Prior radical treatment", "Contraindication to RT"],
    ["OS benefit for low metastatic burden", "Large multi-arm trial"],
    ["No benefit in high-burden disease", "Burden defined by CHAARTED criteria on conventional imaging"],
    "Prostate RT is standard for low-volume mHSPC.")

add("CHAARTED",
    ["Newly diagnosed mHSPC", "ECOG PS 0–2"],
    ["Prior chemotherapy", "ADT started >120 days before randomisation"],
    ["OS benefit for high-volume disease", "Defined high- vs low-volume"],
    ["No benefit in low-volume", "Toxicity (neutropenia, neuropathy)"],
    "Docetaxel benefit is clear in high-volume disease.")

add("LATITUDE / STAMPEDE abiraterone",
    ["High-risk newly diagnosed mHSPC (LATITUDE)", "STAMPEDE: high-risk M0 or M1"],
    ["Prior hormonal therapy", "Uncontrolled hypertension"],
    ["Large OS benefit", "Benefit in both trials"],
    ["Mineralocorticoid side effects (hypertension, hypokalaemia)", "Prednisone needed"],
    "Abiraterone is a standard addition to ADT; low-cost generics make it accessible in India.")

add("TITAN / ENZAMET / ARCHES",
    ["mHSPC", "ECOG PS 0–1"],
    ["Prior ARPI", "Seizure history (enzalutamide)"],
    ["OS benefit across volumes", "Three concordant trials"],
    ["Fatigue and falls", "Cost"],
    "ARPIs with ADT are standard regardless of volume.")

add("PEACE-1 / ARASENS",
    ["De novo mHSPC", "Fit for docetaxel"],
    ["Prior ARPI", "Uncontrolled hypertension"],
    ["OS benefit for triplet therapy", "Consistent across trials"],
    ["Toxicity", "Doublet ARPI comparison lacking"],
    "Triplet therapy is an option for high-volume de novo disease.")

add("SPARTAN / PROSPER / ARAMIS",
    ["nmCRPC with PSA doubling time ≤10 months", "Conventional imaging negative for metastases"],
    ["Metastases on conventional imaging", "Seizure history (apalutamide/enzalutamide)"],
    ["Metastasis-free and OS benefit", "Three concordant trials"],
    ["PSMA-PET would reclassify many patients as metastatic", "Fatigue, falls, rash"],
    "ARPIs are standard for high-risk nmCRPC, though PSMA-PET changes definitions.")

add("EMBARK",
    ["High-risk biochemical recurrence with PSADT ≤9 months", "No metastases on conventional imaging"],
    ["Prior hormonal therapy (within 9 months)", "Seizure history"],
    ["Metastasis-free survival benefit", "Enzalutamide monotherapy arm offered testosterone-sparing option"],
    ["OS immature", "PSMA-PET not used"],
    "Enzalutamide + leuprolide is an option for high-risk BCR.")

add("TAX 327",
    ["mCRPC", "KPS ≥60"],
    ["Prior chemotherapy", "Brain metastases"],
    ["OS benefit", "Large trial"],
    ["Modest gain (~2.5 months)", "Neutropenia"],
    "Docetaxel became the first chemotherapy to improve OS in mCRPC.")

add("COU-AA-301/302, AFFIRM, PREVAIL",
    ["mCRPC pre- or post-docetaxel"],
    ["Prior ARPI", "Visceral metastases (COU-AA-302)"],
    ["OS benefit", "Oral therapy"],
    ["Cross-resistance between ARPIs", "Cost"],
    "ARPIs are standard; sequencing two ARPIs is less effective.")

add("TROPIC / CARD",
    ["mCRPC after docetaxel (and an ARPI in CARD)"],
    ["Prior cabazitaxel", "Grade ≥2 neuropathy"],
    ["OS benefit", "CARD showed superiority over ARPI switch"],
    ["Neutropenia", "G-CSF often needed"],
    "Cabazitaxel is preferred over a second ARPI after docetaxel and one ARPI.")

add("ALSYMPCA",
    ["Symptomatic bone-metastatic CRPC, ≥2 bone metastases", "No visceral metastases"],
    ["Visceral metastases", "Bulky nodes >3 cm"],
    ["OS benefit", "Delayed skeletal events"],
    ["Pre-ARPI era", "Combination with abiraterone increased fractures (ERA 223)"],
    "Radium-223 is an option for bone-only disease.")

add("VISION",
    ["PSMA-PET positive mCRPC", "After ARPI and taxane"],
    ["PSMA-negative lesions", "Prior radioligand therapy"],
    ["OS benefit", "Quality of life benefit"],
    ["Control arm excluded chemotherapy", "Open-label with early dropout in control"],
    "Lu-PSMA is standard in later lines.")

add("PSMAfore",
    ["Taxane-naive PSMA+ mCRPC after one ARPI"],
    ["Prior taxane", "PSMA-negative lesions"],
    ["rPFS benefit", "Better tolerability than taxanes"],
    ["OS confounded by crossover", "Control arm was ARPI switch"],
    "Lu-PSMA is an option before docetaxel.")

add("PROfound",
    ["mCRPC with HRR alterations after ARPI"],
    ["Prior PARP inhibitor", "MDS/AML"],
    ["OS benefit in BRCA1/2, ATM cohort", "Biomarker-driven"],
    ["Benefit driven by BRCA", "Control arm was ARPI switch"],
    "Olaparib is standard for BRCA-mutated mCRPC.")

add("TALAPRO-2 / PROpel",
    ["First-line mCRPC", "ECOG PS 0–1"],
    ["Prior ARPI in mCRPC", "Prior PARP inhibitor"],
    ["rPFS benefit", "Benefit in HRR-mutated"],
    ["Limited benefit in HRR-negative", "Anaemia"],
    "PARPi + ARPI is best for HRR-altered patients.")

add("SWOG 8710",
    ["MIBC T2–T4a", "Fit for cystectomy"],
    ["Distant metastases", "Prior chemotherapy"],
    ["OS benefit", "Long-term follow-up"],
    ["Toxicity", "Slow accrual"],
    "Established neoadjuvant cisplatin-based chemo.")

add("VESPER",
    ["MIBC, cisplatin-eligible", "Fit for cystectomy"],
    ["Distant metastases", "Prior chemotherapy"],
    ["Improved PFS with ddMVAC", "OS signal"],
    ["Toxicity", "Fewer cycles in gem-cis arm"],
    "ddMVAC is a preferred neoadjuvant option.")

add("NIAGARA",
    ["Cisplatin-eligible MIBC", "Fit for cystectomy"],
    ["Prior immunotherapy", "Active autoimmune disease"],
    ["EFS and OS benefit", "Perioperative design"],
    ["Contribution of adjuvant phase unclear", "Immune toxicity"],
    "Perioperative durvalumab is a new standard.")

add("CheckMate 274",
    ["High-risk MIUC after radical surgery", "With or without prior neoadjuvant chemo"],
    ["Prior immunotherapy", "Active autoimmune disease"],
    ["DFS benefit", "Double-blind"],
    ["OS data immature", "Upper tract subgroup less clear"],
    "Adjuvant nivolumab is standard for high-risk resected MIUC.")

add("BC2001",
    ["MIBC T2–T4a", "Suitable for RT"],
    ["Distant metastases", "Prior pelvic RT"],
    ["Improved locoregional control", "Bladder preservation"],
    ["No OS benefit", "Older RT technique"],
    "Chemoradiotherapy with 5-FU/MMC is standard for bladder preservation.")

add("POUT",
    ["Upper-tract urothelial carcinoma pT2–T4 or N+", "Within 90 days of nephroureterectomy"],
    ["Distant metastases", "Prior chemotherapy"],
    ["DFS benefit", "Randomised in rare cancer"],
    ["OS benefit not significant", "Carboplatin used if renal function poor"],
    "Adjuvant chemotherapy is standard for UTUC.")

add("JAVELIN Bladder 100",
    ["Advanced UC without progression after first-line platinum"],
    ["Prior immunotherapy", "Active autoimmune disease"],
    ["OS benefit", "Maintenance strategy"],
    ["Pre-EV/pembro era", "Selected responders"],
    "Avelumab maintenance remains an option after platinum.")

add("EV-302",
    ["Untreated advanced urothelial carcinoma", "Cisplatin-eligible or ineligible"],
    ["Prior systemic therapy", "Active CNS metastases"],
    ["Large OS benefit", "Benefit across subgroups"],
    ["Toxicity (rash, neuropathy, hyperglycaemia)", "Cost"],
    "EV-pembro is the new first-line standard.")

add("CheckMate 901 (gem-cis + nivo)",
    ["Cisplatin-eligible advanced UC", "Treatment-naive"],
    ["Prior systemic therapy", "Active autoimmune disease"],
    ["OS benefit", "Cisplatin-based combination"],
    ["Superseded by EV-302", "Cisplatin-eligible only"],
    "Nivo-gem-cis is an option for cisplatin-eligible patients.")

add("THOR",
    ["FGFR-altered advanced UC after ARPI/IO", "ECOG PS 0–2"],
    ["Prior FGFR inhibitor", "Central serous retinopathy"],
    ["OS benefit", "Biomarker-driven"],
    ["Hyperphosphataemia and eye toxicity", "Requires FGFR testing"],
    "Erdafitinib is standard for FGFR-altered UC.")

add("CheckMate 214",
    ["Advanced clear-cell RCC", "Treatment-naive", "KPS ≥70"],
    ["Brain metastases", "Active autoimmune disease"],
    ["Durable OS benefit in intermediate/poor risk", "Long-term follow-up"],
    ["Immune toxicity", "No benefit in favourable risk"],
    "Nivo-ipi is a standard first-line option.")

add("KEYNOTE-426 / CLEAR / CheckMate 9ER",
    ["Advanced ccRCC", "Treatment-naive", "KPS ≥70"],
    ["Brain metastases", "Active autoimmune disease"],
    ["OS benefit", "High response rates"],
    ["Toxicity of TKIs", "Comparator sunitinib"],
    "IO-TKI combinations are standard.")

add("KEYNOTE-564",
    ["High-risk ccRCC after nephrectomy", "ECOG PS 0–1"],
    ["Distant metastases", "Prior systemic therapy"],
    ["DFS and OS benefit", "Double-blind"],
    ["Toxicity", "Overtreatment of some cured patients"],
    "Adjuvant pembrolizumab is standard.")

add("CARMENA",
    ["Synchronous mRCC, intermediate/poor risk", "Candidates for nephrectomy"],
    ["Prior systemic therapy", "Brain metastases"],
    ["Showed sunitinib alone non-inferior", "Prospective trial"],
    ["Poor accrual", "High-risk patients"],
    "Cytoreductive nephrectomy is not mandatory in intermediate/poor risk.")

add("LITESPARK-005",
    ["Advanced ccRCC after IO and VEGF-TKI", "KPS ≥70"],
    ["Prior HIF-2α inhibitor", "Hypoxia"],
    ["PFS benefit", "Oral therapy"],
    ["OS not significant", "Anaemia and hypoxia"],
    "Belzutifan is an option in later lines.")

add("Einhorn PVB / BEP (Williams)",
    ["Disseminated germ cell tumours", "Adequate organ function"],
    ["Prior chemotherapy", "Poor renal function"],
    ["Reduced toxicity with BEP", "Equivalent efficacy"],
    ["Older trial", "Bleomycin lung toxicity"],
    "BEP is standard for germ cell tumours.")

add("IGCCCG",
    ["Metastatic GCT", "Treated with cisplatin-based chemotherapy"],
    ["None (retrospective)", "Primary mediastinal non-seminoma"],
    ["Defined prognostic groups", "Widely validated"],
    ["Retrospective", "Older data"],
    "Defines risk-adapted therapy.")

add("MRC TE19 (Oliver)",
    ["Stage I seminoma after orchidectomy", "Fit for chemotherapy"],
    ["Prior therapy", "Elevated markers"],
    ["Single-dose carboplatin non-inferior", "Fewer second malignancies"],
    ["Surveillance now preferred", "Low event rate"],
    "Carboplatin is an option; surveillance preferred for low-risk.")
