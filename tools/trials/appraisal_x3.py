# Full-depth rewrites: pancreas, hepatobiliary, NET, prostate.
A = {}
def add(name, inc, exc, pros, cons, critique):
    A[name] = {"inclusion": inc, "exclusion": exc, "strengths": pros, "limitations": cons, "critique": critique}

add("CONKO-001",
    ["Macroscopically complete (R0/R1) resection of pancreatic adenocarcinoma", "No prior chemotherapy or RT", "Postoperative CA19-9 <2.5× upper limit of normal"],
    ["Distant metastases or macroscopic residual disease", "KPS <50"],
    ["First trial to show adjuvant gemcitabine improves DFS and OS", "Long-term data (10-year OS 12.2% vs 7.7%)"],
    ["Small absolute OS gain", "Excluded patients with high post-op CA19-9, a poor-prognosis group"],
    "Established adjuvant chemotherapy after pancreatic resection. Gemcitabine alone is now reserved for patients unfit for mFOLFIRINOX or gem-cap.")

add("ESPAC-4",
    ["Resected pancreatic ductal adenocarcinoma (R0 or R1)", "Randomised within 12 weeks of surgery", "WHO PS 0–2"],
    ["Distant or macroscopic residual disease", "Prior neoadjuvant therapy"],
    ["OS benefit (28.0 vs 25.5 months)", "Pragmatic, included PS 2 patients"],
    ["Small absolute benefit", "OS advantage driven partly by R0 patients"],
    "Gem-cap is the adjuvant regimen for patients not fit for mFOLFIRINOX. With PRODIGE 24 it shows combination therapy beats gemcitabine alone.")

add("PRODIGE 24",
    ["Resected pancreatic adenocarcinoma (R0/R1) within 3–12 weeks", "WHO PS 0–1, age 18–79", "Postoperative CA19-9 ≤180 U/mL"],
    ["Distant metastases", "Prior chemotherapy or RT", "Cardiac disease or poor nutrition"],
    ["Large OS benefit (median 53.5 vs 35.5 months)", "Long-term data confirm durable benefit"],
    ["Fit, selected patients only", "Grade 3–4 toxicity in ~75%", "Many in India are not fit enough post-Whipple"],
    "mFOLFIRINOX is the adjuvant standard for fit patients; dose modifications are common, and patient selection is key.")

add("ACCORD 11 (PRODIGE 4)",
    ["Metastatic pancreatic adenocarcinoma", "ECOG PS 0–1, age ≤75", "Bilirubin ≤1.5× ULN"],
    ["Prior chemotherapy", "Biliary obstruction not stented", "Brain metastases"],
    ["Large OS benefit (11.1 vs 6.8 months)", "First regimen to beat gemcitabine by a wide margin"],
    ["Significant toxicity (neutropenia, neuropathy, diarrhoea)", "Fit, younger patients only", "French centres only"],
    "FOLFIRINOX is standard for fit patients with metastatic disease. Modified doses are used widely to improve tolerability.")

add("MPACT",
    ["Metastatic pancreatic adenocarcinoma", "KPS ≥70", "No prior treatment for metastatic disease"],
    ["Prior chemotherapy", "Neuropathy grade ≥2"],
    ["OS benefit (8.5 vs 6.7 months)", "Broader eligibility than FOLFIRINOX (KPS ≥70)"],
    ["Neuropathy", "Modest benefit"],
    "Gem-nab-paclitaxel is standard for patients who cannot tolerate FOLFIRINOX. No head-to-head comparison with FOLFIRINOX exists.")

add("NAPOLI-3",
    ["Metastatic pancreatic adenocarcinoma", "Treatment-naive", "ECOG PS 0–1"],
    ["Prior systemic therapy", "Brain metastases"],
    ["OS benefit over gem-nab-paclitaxel (11.1 vs 9.2 months)"],
    ["No comparison with FOLFIRINOX", "Liposomal irinotecan expensive"],
    "NALIRIFOX is an option, but many view it as FOLFIRINOX with a costlier irinotecan; FOLFIRINOX remains equally reasonable.")

add("POLO",
    ["Germline BRCA1/2-mutated metastatic pancreatic cancer", "No progression after ≥16 weeks of first-line platinum"],
    ["Progression on platinum", "Prior PARP inhibitor"],
    ["PFS benefit (7.4 vs 3.8 months)", "Biomarker-driven maintenance"],
    ["No OS benefit", "Placebo comparator; continuing platinum not tested", "Small group eligible (~4–7%)"],
    "Olaparib maintenance gives a chemotherapy break but no proven survival gain; continuing platinum is a reasonable alternative. Germline testing for all pancreatic cancers is supported.")

add("RASolute 302",
    ["Metastatic pancreatic adenocarcinoma progressing after one prior line of therapy", "ECOG PS 0–1"],
    ["Prior RAS-directed therapy", "Untreated brain metastases"],
    ["OS benefit (~13 vs 7 months) for a RAS(ON) inhibitor", "Benefit across common KRAS variants"],
    ["Recent data — long-term toxicity and durability still emerging", "Subgroups with rare mutations imprecise"],
    "Daraxonrasib appears to be a major advance in second-line PDAC; real-world availability and cost in India are yet to be defined.")

add("PREOPANC",
    ["Resectable or borderline resectable pancreatic adenocarcinoma", "WHO PS 0–1"],
    ["Distant metastases", "Prior therapy"],
    ["Long-term OS benefit for neoadjuvant chemoRT", "Included resectable and borderline disease"],
    ["Gemcitabine-based regimen — not modern multi-agent chemotherapy", "Primary OS endpoint not significant initially; benefit emerged with longer follow-up"],
    "Supports a neoadjuvant approach, especially for borderline resectable disease. PREOPANC-2 and others test FOLFIRINOX-based strategies.")

add("SHARP",
    ["Advanced HCC not amenable to surgery or locoregional therapy", "Child-Pugh A", "ECOG PS 0–2"],
    ["Prior systemic therapy", "Child-Pugh B or C"],
    ["First systemic therapy to improve OS in HCC (10.7 vs 7.9 months)"],
    ["Modest benefit", "Hand-foot skin reaction and diarrhoea", "Mainly HCV-related HCC in Europe"],
    "Established systemic therapy for HCC; now superseded by IO combinations but still used where IO is unaffordable.")

add("REFLECT",
    ["Unresectable HCC, Child-Pugh A", "BCLC B or C", "ECOG PS 0–1"],
    ["≥50% liver involvement", "Main portal vein invasion", "Bile duct invasion"],
    ["Non-inferior OS to sorafenib with better PFS and response"],
    ["Excluded high-risk patients (main portal vein invasion)", "Hypertension and proteinuria"],
    "Lenvatinib is an alternative first-line option when immunotherapy is not suitable.")

add("IMbrave150",
    ["Unresectable HCC, Child-Pugh A", "Treatment-naive for systemic therapy", "ECOG PS 0–1"],
    ["Untreated or incompletely treated varices with bleeding risk", "Autoimmune disease", "Main portal vein thrombosis with high risk (some)"],
    ["OS benefit (19.2 vs 13.4 months)", "Improved quality of life"],
    ["Bleeding risk requiring endoscopy before treatment", "Benefit less in non-viral HCC"],
    "Atezolizumab-bevacizumab is the first-line standard. Upper GI endoscopy and variceal management must precede treatment.")

add("HIMALAYA",
    ["Unresectable HCC, Child-Pugh A", "BCLC B or C", "Treatment-naive"],
    ["Main portal vein thrombosis", "Active GI bleeding"],
    ["Durable OS benefit with long follow-up", "No bleeding risk from anti-VEGF"],
    ["Immune toxicity", "Single priming dose of tremelimumab may be impractical in some settings"],
    "STRIDE is an option for patients with bleeding risk or contraindications to bevacizumab.")

add("CheckMate 9DW",
    ["Unresectable HCC, Child-Pugh A", "Treatment-naive", "ECOG PS 0–1"],
    ["Prior systemic therapy", "Active autoimmune disease"],
    ["OS benefit over lenvatinib or sorafenib"],
    ["Immune toxicity, including hepatitis"],
    "Nivo-ipi is another first-line option; choice among IO regimens depends on comorbidities and access.")

add("TOPAZ-1",
    ["Advanced biliary tract cancer (intrahepatic, extrahepatic, gallbladder)", "Treatment-naive", "ECOG PS 0–1"],
    ["Prior systemic therapy", "Ampullary carcinoma"],
    ["OS benefit (12.8 vs 11.5 months)", "Long-term survivors"],
    ["Modest median gain", "Benefit less in gallbladder cancer"],
    "Durvalumab-gem-cis is first-line standard; relevant to India where gallbladder cancer is common.")

add("ABC-02",
    ["Advanced biliary tract cancer", "ECOG PS 0–2"],
    ["Prior chemotherapy"],
    ["OS benefit (11.7 vs 8.1 months)"],
    ["Pre-IO era"],
    "Established gem-cis as standard backbone for advanced biliary cancer.")

add("BILCAP",
    ["Resected biliary tract cancer (R0/R1)", "ECOG PS 0–2"],
    ["Distant metastases", "Prior therapy"],
    ["OS benefit in per-protocol analysis"],
    ["ITT OS difference not significant", "Heterogeneous biliary sites"],
    "Capecitabine is standard adjuvant therapy, though the evidence is modest.")

add("ClarIDHy / FIGHT-202",
    ["IDH1-mutant (ClarIDHy) or FGFR2-fusion (FIGHT-202) cholangiocarcinoma", "Previously treated"],
    ["Prior targeted therapy against same target"],
    ["Established targeted therapy in biliary cancer"],
    ["FIGHT-202 single-arm", "Modest PFS in ClarIDHy; OS benefit only after crossover adjustment"],
    "Supports molecular testing in intrahepatic cholangiocarcinoma.")

add("NETTER-1",
    ["SSTR-positive midgut NET, grade 1–2", "Progressing on octreotide LAR 30 mg"],
    ["Prior PRRT", "Kidney dysfunction"],
    ["Large PFS benefit (HR ~0.18)", "Quality-of-life benefit"],
    ["Open-label", "OS difference not statistically significant"],
    "PRRT is the standard second-line therapy for midgut NET.")

add("NETTER-2",
    ["Newly diagnosed SSTR+ grade 2/3 GEP-NET (Ki-67 10–55%)"],
    ["Prior PRRT", "Poorly differentiated carcinoma"],
    ["PFS benefit in first line"],
    ["OS immature", "High-dose octreotide control"],
    "First-line PRRT is an option for higher-grade NETs.")

add("PROMID / CLARINET",
    ["Well-differentiated GEP-NET (midgut in PROMID; GEP-NET with Ki-67 <10% in CLARINET)"],
    ["Prior SSA", "Poorly differentiated tumours"],
    ["PFS benefit", "Well tolerated"],
    ["No OS benefit", "Mostly low-grade tumours"],
    "SSAs are first-line therapy for well-differentiated NETs.")

add("RADIANT-3/4 & SUN-1111",
    ["Advanced pancreatic (RADIANT-3, SUN) or lung/GI NET (RADIANT-4)", "Progressive disease"],
    ["Prior mTOR or VEGF therapy", "Poorly differentiated tumours"],
    ["PFS benefit"],
    ["No OS benefit", "Stomatitis, hyperglycaemia (everolimus); hypertension (sunitinib)"],
    "Everolimus and sunitinib are options after SSAs.")

add("E2211 (CAPTEM)",
    ["Advanced pancreatic NET", "Progressive within 12 months"],
    ["Prior temozolomide or dacarbazine"],
    ["PFS and OS benefit"],
    ["Myelosuppression"],
    "CAPTEM is an effective option for pancreatic NETs.")

# Prostate
add("RTOG 94-08",
    ["Localised prostate cancer T1b–T2b", "PSA ≤20 ng/mL", "No nodal or distant disease"],
    ["High-risk features (T3, Gleason 8–10 in many)", "Prior hormonal therapy"],
    ["OS benefit for short-term ADT with RT (10-year OS 62% vs 57%)", "Large trial (n=1,979)"],
    ["RT dose 66.6 Gy — below modern dose-escalated standards", "Benefit confined to intermediate risk"],
    "Short-course ADT benefits intermediate-risk disease; with modern dose escalation its magnitude is debated, and favourable intermediate risk may skip it.")

add("Bolla EORTC 22863",
    ["Locally advanced (T3–4) or high-grade T1–2 prostate cancer", "WHO PS 0–2"],
    ["Distant metastases", "Prior hormonal therapy"],
    ["OS benefit for long-term ADT with RT", "10-year follow-up"],
    ["Low RT dose (70 Gy)", "ADT side effects (metabolic, bone)"],
    "Established long-term ADT with RT for high-risk disease; duration (18–36 months) remains individualised.")

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
    ["Higher acute GU toxicity in HYPO-RT-PC"],
    "Ultra-hypofractionation (5 fractions) is a standard option for low-intermediate risk.")

add("ASCENDE-RT",
    ["Intermediate or high-risk localised prostate cancer"],
    ["Distant metastases", "Prior TURP"],
    ["Improved biochemical control with LDR boost"],
    ["Higher GU toxicity", "No OS benefit"],
    "Brachytherapy boost improves PSA control but at higher urinary toxicity cost.")

add("RADICALS-RT / RAVES / GETUG-AFU 17 (ARTISTIC)",
    ["After radical prostatectomy with adverse features (pT3/4, positive margins)", "Post-op PSA ≤0.2 ng/mL"],
    ["Pelvic nodal metastases (some)", "Prior hormonal therapy"],
    ["Meta-analysis showed early salvage equivalent to adjuvant RT", "Avoided overtreatment in ~half"],
    ["Few very high-risk patients (pN1, Gleason 8–10)"],
    "Early salvage RT is preferred; adjuvant RT for very high-risk features remains debated.")

add("STAMPEDE (arm H) M1 RT",
    ["Newly diagnosed metastatic hormone-sensitive prostate cancer", "WHO PS 0–2"],
    ["Prior radical treatment", "Contraindication to RT"],
    ["OS benefit for low metastatic burden"],
    ["No benefit in high-burden disease", "Burden defined by CHAARTED criteria on conventional imaging"],
    "Prostate RT is standard for low-volume mHSPC.")

add("CHAARTED",
    ["Newly diagnosed mHSPC", "ECOG PS 0–2"],
    ["Prior chemotherapy", "ADT started >120 days before randomisation"],
    ["OS benefit for high-volume disease"],
    ["No benefit in low-volume", "Toxicity (neutropenia, neuropathy)"],
    "Docetaxel benefit is clear in high-volume disease.")

add("LATITUDE / STAMPEDE abiraterone",
    ["High-risk newly diagnosed mHSPC (LATITUDE)", "STAMPEDE: high-risk M0 or M1"],
    ["Prior hormonal therapy", "Uncontrolled hypertension"],
    ["Large OS benefit"],
    ["Mineralocorticoid side effects (hypertension, hypokalaemia)"],
    "Abiraterone is a standard addition to ADT; low-cost generics make it accessible in India.")

add("TITAN / ENZAMET / ARCHES",
    ["mHSPC", "ECOG PS 0–1"],
    ["Prior ARPI", "Seizure history (enzalutamide)"],
    ["OS benefit across volumes"],
    ["Fatigue and falls"],
    "ARPIs with ADT are standard regardless of volume.")

add("PEACE-1 / ARASENS",
    ["De novo mHSPC", "Fit for docetaxel"],
    ["Prior ARPI", "Uncontrolled hypertension"],
    ["OS benefit for triplet therapy"],
    ["Toxicity", "Doublet ARPI comparison lacking"],
    "Triplet therapy is an option for high-volume de novo disease.")

add("SPARTAN / PROSPER / ARAMIS",
    ["nmCRPC with PSA doubling time ≤10 months", "Conventional imaging negative for metastases"],
    ["Metastases on conventional imaging", "Seizure history (apalutamide/enzalutamide)"],
    ["Metastasis-free and OS benefit"],
    ["PSMA-PET would reclassify many patients as metastatic"],
    "ARPIs are standard for high-risk nmCRPC, though PSMA-PET changes definitions.")

add("EMBARK",
    ["High-risk biochemical recurrence with PSADT ≤9 months", "No metastases on conventional imaging"],
    ["Prior hormonal therapy (within 9 months)", "Seizure history"],
    ["Metastasis-free survival benefit"],
    ["OS immature", "PSMA-PET not used"],
    "Enzalutamide + leuprolide is an option for high-risk BCR.")

add("TAX 327",
    ["mCRPC", "KPS ≥60"],
    ["Prior chemotherapy", "Brain metastases"],
    ["OS benefit"],
    ["Modest gain (~2.5 months)"],
    "Docetaxel became the first chemotherapy to improve OS in mCRPC.")

add("COU-AA-301/302, AFFIRM, PREVAIL",
    ["mCRPC pre- or post-docetaxel"],
    ["Prior ARPI", "Visceral metastases (COU-AA-302)"],
    ["OS benefit"],
    ["Cross-resistance between ARPIs"],
    "ARPIs are standard; sequencing two ARPIs is less effective.")

add("TROPIC / CARD",
    ["mCRPC after docetaxel (and an ARPI in CARD)"],
    ["Prior cabazitaxel", "Grade ≥2 neuropathy"],
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
    ["PSMA-negative lesions", "Prior radioligand therapy"],
    ["OS benefit"],
    ["Control arm excluded chemotherapy"],
    "Lu-PSMA is standard in later lines.")

add("PSMAfore",
    ["Taxane-naive PSMA+ mCRPC after one ARPI"],
    ["Prior taxane", "PSMA-negative lesions"],
    ["rPFS benefit"],
    ["OS confounded by crossover"],
    "Lu-PSMA is an option before docetaxel.")

add("PROfound",
    ["mCRPC with HRR alterations after ARPI"],
    ["Prior PARP inhibitor", "MDS/AML"],
    ["OS benefit in BRCA1/2, ATM cohort"],
    ["Benefit driven by BRCA"],
    "Olaparib is standard for BRCA-mutated mCRPC.")

add("TALAPRO-2 / PROpel",
    ["First-line mCRPC", "ECOG PS 0–1"],
    ["Prior ARPI in mCRPC", "Prior PARP inhibitor"],
    ["rPFS benefit", "Benefit in HRR-mutated"],
    ["Limited benefit in HRR-negative"],
    "PARPi + ARPI is best for HRR-altered patients.")
