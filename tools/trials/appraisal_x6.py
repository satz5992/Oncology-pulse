# Depth pass: colorectal, anal, pancreas, hepatobiliary, NET.
A = {}
def add(name, inc, exc, pros, cons, critique):
    A[name] = {"inclusion": inc, "exclusion": exc, "strengths": pros, "limitations": cons, "critique": critique}

add("OPRA",
    ["Stage II–III rectal adenocarcinoma on MRI", "Candidates for TME surgery", "ECOG PS 0–1"],
    ["Distant metastases", "Prior pelvic RT", "Tumours not suitable for watch-and-wait follow-up"],
    ["Organ preservation in about half with consolidation chemotherapy", "Structured watch-and-wait protocol"],
    ["Phase 2 with comparison to historical TME outcomes", "Regrowth in ~a third of watched patients needs salvage surgery"],
    "Watch-and-wait after consolidation TNT is feasible, but it demands rigorous MRI and endoscopic surveillance that many centres cannot provide.")

add("PROSPECT",
    ["cT2N+ or cT3N0–1 rectal cancer", "Candidates for sphincter-sparing surgery", "MRI-staged"],
    ["cT4 disease", "Low tumours requiring APR", "Distant metastases"],
    ["Showed FOLFOX alone (with selective chemoRT) is non-inferior for DFS", "Less long-term bowel and sexual toxicity"],
    ["Only intermediate-risk patients", "Requires high-quality MRI staging", "~9% still needed chemoRT"],
    "Pelvic RT can be omitted in selected intermediate-risk rectal cancer, sparing fertility and late bowel effects.")

add("CRYSTAL",
    ["Metastatic CRC, first line", "EGFR-expressing tumour", "ECOG PS 0–2"],
    ["Prior systemic therapy for metastatic disease", "Prior anti-EGFR therapy"],
    ["OS benefit in KRAS wild-type", "Large trial enabling biomarker discovery"],
    ["Retrospective biomarker analysis", "Acneiform rash and hypomagnesaemia"],
    "Established anti-EGFR therapy for RAS wild-type mCRC and helped define RAS testing.")

add("FIRE-3 / CALGB 80405",
    ["RAS wild-type metastatic CRC (on extended analysis)", "Treatment-naive", "ECOG PS 0–2"],
    ["Prior systemic therapy for metastatic disease", "Contraindication to bevacizumab"],
    ["Head-to-head comparison of biologics", "Generated the primary-sidedness hypothesis"],
    ["Primary endpoints (ORR, OS) not met overall", "Sidedness analysis retrospective"],
    "Anti-EGFR is preferred for left-sided RAS wild-type tumours; bevacizumab for right-sided.")

add("PARADIGM",
    ["RAS wild-type metastatic CRC", "Treatment-naive", "ECOG PS 0–1"],
    ["BRAF V600E mutation", "Prior systemic therapy"],
    ["Prospective confirmation of left-sided OS benefit for panitumumab", "Primary endpoint in left-sided population"],
    ["Japanese population only", "No benefit for right-sided tumours"],
    "Panitumumab-FOLFOX is standard for left-sided RAS/BRAF wild-type mCRC.")

add("KEYNOTE-177",
    ["MSI-H/dMMR metastatic CRC", "Treatment-naive", "ECOG PS 0–1"],
    ["Prior systemic therapy for metastatic disease", "Active autoimmune disease"],
    ["Doubled PFS", "Better quality of life and fewer severe adverse events"],
    ["Early progression in ~30%", "OS not statistically significant due to crossover"],
    "Pembrolizumab is first-line standard for MSI-H mCRC; early progressors (possibly misclassified MMR status) need attention.")

add("CheckMate 8HW",
    ["MSI-H/dMMR metastatic CRC", "ECOG PS 0–1"],
    ["Prior immunotherapy", "Active autoimmune disease"],
    ["Superior PFS with dual IO vs chemotherapy and vs nivolumab alone"],
    ["More immune toxicity", "OS immature"],
    "Nivolumab-ipilimumab is an option, weighing durability against immune toxicity.")

add("BEACON CRC / BREAKWATER",
    ["BRAF V600E metastatic CRC", "BEACON: after 1–2 lines; BREAKWATER: first line", "ECOG PS 0–1"],
    ["Prior BRAF/EGFR inhibitor", "Active brain metastases"],
    ["OS benefit in a poor-prognosis group", "Better than standard chemotherapy"],
    ["Triplet arm (with binimetinib) not superior in BEACON", "Cost"],
    "Encorafenib-cetuximab is standard; first-line combination with FOLFOX is now emerging.")

add("DESTINY-CRC / MOUNTAINEER",
    ["HER2-positive, RAS wild-type metastatic CRC", "Previously treated", "ECOG PS 0–1"],
    ["Prior anti-HER2 therapy", "History of ILD (DESTINY-CRC)"],
    ["High response rates in a chemotherapy-refractory group", "Oral tucatinib combination well tolerated"],
    ["Single-arm", "ILD risk with T-DXd"],
    "Supports HER2 testing in RAS wild-type mCRC; randomised data are limited.")

add("CORRECT / RECOURSE / SUNLIGHT",
    ["Refractory metastatic CRC", "Prior fluoropyrimidine, oxaliplatin, irinotecan, anti-VEGF ± anti-EGFR", "ECOG PS 0–1"],
    ["Prior regorafenib or FTD-TPI (by trial)", "ECOG PS ≥2"],
    ["OS benefit", "SUNLIGHT showed added benefit with bevacizumab"],
    ["Modest gains", "Toxicity (regorafenib hand-foot syndrome)"],
    "FTD-TPI + bevacizumab is preferred; regorafenib remains an option.")

add("FRESCO-2",
    ["Refractory metastatic CRC after standard therapies including FTD-TPI or regorafenib", "ECOG PS 0–1"],
    ["Prior fruquintinib", "Uncontrolled hypertension"],
    ["OS benefit in heavily pretreated patients", "Global population"],
    ["Modest benefit (~2.6 months)", "Hypertension and fatigue"],
    "Fruquintinib is an additional late-line option.")

add("EORTC 40983 (EPOC)",
    ["Resectable colorectal liver metastases (≤4)", "No extrahepatic disease", "WHO PS 0–2"],
    ["Prior oxaliplatin", "Extrahepatic disease"],
    ["PFS benefit", "Perioperative design"],
    ["No OS benefit", "Underpowered"],
    "Perioperative FOLFOX is reasonable; OS benefit unproven.")

add("ACT II",
    ["Anal SCC, non-metastatic", "Age ≥18", "WHO PS 0–2"],
    ["Prior pelvic RT", "Distant metastases"],
    ["Large trial (n=940)", "Showed maintenance chemo not needed"],
    ["Few HIV-positive patients", "Assessment at 26 weeks — earlier assessment can lead to unnecessary surgery"],
    "5-FU/mitomycin with RT remains standard. The finding that responses can take 26 weeks prevents premature salvage surgery.")

add("RTOG 98-11",
    ["Anal SCC T2–4, any N", "Non-metastatic"],
    ["Distant metastases", "Prior pelvic RT"],
    ["Showed cisplatin induction inferior", "Long-term follow-up"],
    ["Induction delayed RT", "Not designed to test cisplatin without induction"],
    "Confirmed mitomycin-based chemoRT as standard.")

add("POD1UM-303",
    ["Advanced anal SCC", "Treatment-naive", "ECOG PS 0–1"],
    ["Prior immunotherapy", "Active autoimmune disease"],
    ["PFS benefit", "First positive IO trial in anal cancer"],
    ["OS immature", "Modest PFS gain"],
    "Adds retifanlimab to first-line carboplatin-paclitaxel.")

add("MPACT",
    ["Metastatic pancreatic adenocarcinoma", "KPS ≥70", "No prior treatment for metastatic disease"],
    ["Prior chemotherapy", "Neuropathy grade ≥2"],
    ["OS benefit (8.5 vs 6.7 months)", "Broader eligibility than FOLFIRINOX (KPS ≥70)"],
    ["Neuropathy", "Modest benefit"],
    "Gem-nab-paclitaxel is standard for patients who cannot tolerate FOLFIRINOX. No head-to-head comparison with FOLFIRINOX exists.")

add("NAPOLI-3",
    ["Metastatic pancreatic adenocarcinoma", "Treatment-naive", "ECOG PS 0–1"],
    ["Prior systemic therapy", "Brain metastases"],
    ["OS benefit over gem-nab-paclitaxel (11.1 vs 9.2 months)", "Large global trial"],
    ["No comparison with FOLFIRINOX", "Liposomal irinotecan is expensive"],
    "NALIRIFOX is an option, but many view it as FOLFIRINOX with a costlier irinotecan; FOLFIRINOX remains equally reasonable.")

add("PREOPANC",
    ["Resectable or borderline resectable pancreatic adenocarcinoma", "WHO PS 0–1"],
    ["Distant metastases", "Prior therapy"],
    ["Long-term OS benefit for neoadjuvant chemoRT", "Included resectable and borderline disease"],
    ["Gemcitabine-based regimen — not modern multi-agent chemotherapy", "OS benefit emerged only with longer follow-up"],
    "Supports a neoadjuvant approach, especially for borderline resectable disease. PREOPANC-2 tests FOLFIRINOX-based strategies.")

add("SHARP",
    ["Advanced HCC not amenable to surgery or locoregional therapy", "Child-Pugh A", "ECOG PS 0–2"],
    ["Prior systemic therapy", "Child-Pugh B or C"],
    ["First systemic therapy to improve OS in HCC (10.7 vs 7.9 months)", "Double-blind"],
    ["Modest benefit", "Hand-foot skin reaction and diarrhoea", "Mainly HCV-related HCC in Europe"],
    "Established systemic therapy for HCC; now superseded by IO combinations but still used where IO is unaffordable.")

add("REFLECT",
    ["Unresectable HCC, Child-Pugh A", "BCLC B or C", "ECOG PS 0–1"],
    ["≥50% liver involvement", "Main portal vein invasion", "Bile duct invasion"],
    ["Non-inferior OS to sorafenib with better PFS and response", "Large Asian representation"],
    ["Excluded high-risk patients (main portal vein invasion)", "Hypertension and proteinuria"],
    "Lenvatinib is an alternative first-line option when immunotherapy is not suitable.")

add("HIMALAYA",
    ["Unresectable HCC, Child-Pugh A", "BCLC B or C", "Treatment-naive"],
    ["Main portal vein thrombosis", "Active GI bleeding"],
    ["Durable OS benefit with long follow-up", "No bleeding risk from anti-VEGF"],
    ["Immune toxicity", "Single priming dose of tremelimumab may be impractical in some settings"],
    "STRIDE is an option for patients with bleeding risk or contraindications to bevacizumab.")

add("CheckMate 9DW",
    ["Unresectable HCC, Child-Pugh A", "Treatment-naive", "ECOG PS 0–1"],
    ["Prior systemic therapy", "Active autoimmune disease"],
    ["OS benefit over lenvatinib or sorafenib", "Durable responses"],
    ["Immune toxicity, including hepatitis", "Higher early death rate in IO arm"],
    "Nivo-ipi is another first-line option; choice among IO regimens depends on comorbidities and access.")

add("TOPAZ-1",
    ["Advanced biliary tract cancer (intrahepatic, extrahepatic, gallbladder)", "Treatment-naive", "ECOG PS 0–1"],
    ["Prior systemic therapy", "Ampullary carcinoma"],
    ["OS benefit (12.8 vs 11.5 months)", "Long-term survivors"],
    ["Modest median gain", "Benefit less in gallbladder cancer"],
    "Durvalumab-gem-cis is first-line standard; relevant to India where gallbladder cancer is common.")

add("ABC-02",
    ["Advanced biliary tract cancer", "ECOG PS 0–2"],
    ["Prior chemotherapy", "Uncontrolled biliary obstruction"],
    ["OS benefit (11.7 vs 8.1 months)", "Established gem-cis backbone"],
    ["Pre-IO era", "Heterogeneous biliary sites"],
    "Established gem-cis as standard backbone for advanced biliary cancer.")

add("BILCAP",
    ["Resected biliary tract cancer (R0/R1)", "ECOG PS 0–2"],
    ["Distant metastases", "Prior therapy"],
    ["OS benefit in per-protocol analysis", "Low-cost oral therapy"],
    ["ITT OS difference not significant", "Heterogeneous biliary sites"],
    "Capecitabine is standard adjuvant therapy, though the evidence is modest.")

add("ClarIDHy / FIGHT-202",
    ["IDH1-mutant (ClarIDHy) or FGFR2-fusion (FIGHT-202) cholangiocarcinoma", "Previously treated", "ECOG PS 0–1"],
    ["Prior targeted therapy against same target"],
    ["Established targeted therapy in biliary cancer", "Well tolerated oral agents"],
    ["FIGHT-202 single-arm", "Modest PFS in ClarIDHy; OS benefit only after crossover adjustment"],
    "Supports molecular testing in intrahepatic cholangiocarcinoma.")

add("NETTER-1",
    ["SSTR-positive midgut NET, grade 1–2", "Progressing on octreotide LAR 30 mg"],
    ["Prior PRRT", "Kidney dysfunction"],
    ["Large PFS benefit (HR ~0.18)", "Quality-of-life benefit"],
    ["Open-label", "OS difference not statistically significant"],
    "PRRT is the standard second-line therapy for midgut NET.")

add("NETTER-2",
    ["Newly diagnosed SSTR+ grade 2/3 GEP-NET (Ki-67 10–55%)", "SSTR-positive on imaging"],
    ["Prior PRRT", "Poorly differentiated carcinoma"],
    ["PFS benefit in first line", "Higher response rate"],
    ["OS immature", "High-dose octreotide control"],
    "First-line PRRT is an option for higher-grade NETs.")

add("PROMID / CLARINET",
    ["Well-differentiated GEP-NET (midgut in PROMID; GEP-NET with Ki-67 <10% in CLARINET)", "SSTR-positive (CLARINET)"],
    ["Prior SSA", "Poorly differentiated tumours"],
    ["PFS benefit", "Well tolerated"],
    ["No OS benefit", "Mostly low-grade tumours"],
    "SSAs are first-line therapy for well-differentiated NETs.")

add("RADIANT-3/4 & SUN-1111",
    ["Advanced pancreatic (RADIANT-3, SUN) or lung/GI NET (RADIANT-4)", "Progressive disease"],
    ["Prior mTOR or VEGF therapy", "Poorly differentiated tumours"],
    ["PFS benefit", "Oral agents"],
    ["No OS benefit", "Stomatitis, hyperglycaemia (everolimus); hypertension (sunitinib)"],
    "Everolimus and sunitinib are options after SSAs.")

add("E2211 (CAPTEM)",
    ["Advanced pancreatic NET", "Progressive within 12 months"],
    ["Prior temozolomide or dacarbazine", "Poorly differentiated tumours"],
    ["PFS and OS benefit", "Oral regimen"],
    ["Myelosuppression", "Phase 2 design"],
    "CAPTEM is an effective option for pancreatic NETs.")
