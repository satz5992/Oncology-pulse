# Critical appraisal for breast trials: key eligibility, strengths, limitations, critique.
# Keyed by the exact trial "name" used in breast.py. Revision aid; verify against the primary paper.
A = {}
def add(name, inc, exc, pros, cons, critique):
    A[name] = {"inclusion": inc, "exclusion": exc, "strengths": pros, "limitations": cons, "critique": critique}

add("NSABP B-06",
    ["Stage I–II invasive breast cancer, tumour ≤4 cm", "Clinically mobile axillary nodes allowed", "Tumour excisable with acceptable cosmesis"],
    ["Fixed or matted axillary nodes", "Skin or chest-wall involvement", "Prior breast cancer"],
    ["Large randomised trial with 20-year follow-up", "Three-arm design isolated the effect of RT after lumpectomy"],
    ["Pre-dates modern imaging, systemic therapy and margin standards", "Data-integrity scandal at one site (reanalysis confirmed results)", "Only node-positive patients received chemotherapy (melphalan-5FU)"],
    "Foundational proof that breast conservation plus RT is equivalent to mastectomy for survival. Absolute recurrence rates without RT are far higher than in today's well-staged, systemically treated patients, so the size of the RT benefit is overstated for modern practice.")

add("Milan I (Veronesi)",
    ["Invasive breast cancer ≤2 cm", "Clinically node-negative", "Age <70 years"],
    ["Multicentric disease", "Prior malignancy", "Tumour in subareolar region"],
    ["Single-institution randomised trial with 20-year follow-up", "Low loss to follow-up"],
    ["Small tumours only; single centre", "Quadrantectomy is more extensive than modern lumpectomy", "No systemic therapy for node-negative patients"],
    "Together with B-06 it established breast conservation. Results apply to small tumours; the extensive quadrantectomy and boost used make it less directly comparable with today's margin-directed lumpectomy.")

add("EBCTCG RT overview",
    ["Randomised trials of RT vs no RT after breast-conserving surgery", "Individual patient data from 17 trials", "Women with invasive breast cancer, pN0 or pN+"],
    ["Non-randomised studies", "Trials of DCIS (analysed separately)"],
    ["Individual patient-level meta-analysis — highest level of evidence", "Links recurrence reduction to mortality benefit (~1 death avoided per 4 recurrences prevented)"],
    ["Many trials used old RT techniques and no modern systemic therapy", "Heterogeneous surgery, margins and RT doses", "Cannot identify subgroups who safely omit RT in modern era"],
    "Robust demonstration that local control matters for survival. Absolute benefits in modern low-risk patients on endocrine therapy are smaller, which is why omission trials (PRIME II, CALGB 9343) followed.")

add("START-B",
    ["Women with early invasive breast cancer (pT1–3a, pN0–1)", "After BCS or mastectomy", "Requiring breast or chest-wall RT"],
    ["Immediate reconstruction", "Need for nodal RT in most protocols (allowed but uncommon)", "Distant metastases"],
    ["Large, multicentre, pragmatic trial with 10-year follow-up", "Measured photographic and patient-reported late effects"],
    ["Mostly lower-risk, node-negative patients", "Boost use was variable", "Limited data for nodal RT and reconstruction"],
    "Practice-changing: 40 Gy/15 is at least as effective with fewer late effects than 50 Gy/25. Applicability to nodal RT and reconstruction relied on later trials.")

add("FAST-Forward",
    ["Invasive breast cancer pT1–3, pN0–1, M0", "After BCS or mastectomy (no reconstruction)", "Age ≥18"],
    ["Immediate reconstruction", "Nodal RT required (separate nodal sub-study)", "Prior thoracic RT"],
    ["Large non-inferiority trial with 5-year (and 10-year) data", "Detailed clinician, patient and photographic normal-tissue assessment"],
    ["Low event rate — non-inferiority margins applied to small absolute numbers", "Mostly low-risk, node-negative patients", "Limited data on boost, nodal RT and reconstruction"],
    "Shows 26 Gy/5 fractions is non-inferior with similar toxicity, saving 2 weeks of travel — highly relevant in India. Concerns remain about generalising to nodal RT, reconstruction and large breasts.")

add("EORTC 22881 Boost",
    ["Stage I–II breast cancer after lumpectomy with microscopically complete excision", "Received 50 Gy whole-breast RT", "Age ≤70"],
    ["Incomplete excision (randomised separately)", "Prior breast cancer", "Distant metastases"],
    ["Very large trial with 20-year follow-up", "Clear age-stratified absolute benefit"],
    ["Boost increased severe fibrosis", "No survival benefit", "Pre-dates modern margins and systemic therapy"],
    "Boost roughly halves local recurrence relative risk but the absolute gain is small in older women; it supports selective boosting (young age, high grade) rather than boosting everyone.")

add("MA.20",
    ["Node-positive (or high-risk node-negative) after BCS", "Adjuvant chemotherapy and/or endocrine therapy as indicated", "Planned whole-breast RT"],
    ["Prior mastectomy", "T4 disease", "Distant metastases"],
    ["Randomised evidence for regional nodal irradiation", "10-year follow-up"],
    ["No overall survival benefit", "More pneumonitis and lymphoedema", "Mostly 1–3 node positive women"],
    "Regional nodal RT improved disease-free survival but not OS. Its main value is in reducing regional and distant recurrence, which must be balanced against lymphoedema and lung toxicity.")

add("EORTC 22922",
    ["Stage I–III breast cancer", "Medial/central tumours or axillary node involvement", "BCS or mastectomy"],
    ["Distant metastases", "Prior RT", "Neoadjuvant therapy in early years"],
    ["Large international trial, 15-year follow-up", "Internal mammary RT tested directly"],
    ["OS benefit modest and not statistically significant at 10 years", "Older RT techniques with possible cardiac dose", "Heterogeneous population"],
    "Supports IMN-medial supraclavicular RT for high-risk patients. Benefits are small and must be weighed against cardiac dose, especially with left-sided tumours.")

add("Danish 82b/82c & EBCTCG PMRT",
    ["Mastectomy with axillary dissection", "High-risk: node-positive, tumour >5 cm or skin/fascia invasion", "Pre- (82b, with CMF) or postmenopausal (82c, with tamoxifen)"],
    ["Distant metastases", "Prior malignancy"],
    ["Showed overall survival benefit from post-mastectomy RT", "Confirmed by EBCTCG meta-analysis even for 1–3 positive nodes"],
    ["Inadequate axillary dissection (median ~7 nodes) inflated regional recurrence", "Systemic therapy below modern standards", "Older RT technique"],
    "Practice-defining for PMRT, but the high locoregional recurrence in controls partly reflected limited axillary surgery. In 1–3 node-positive disease today the absolute gain is smaller.")

add("CALGB 9343",
    ["Women ≥70 years", "T1N0 (clinically), ER-positive or unknown", "Lumpectomy with clear margins"],
    ["Tumour >2 cm", "Clinically positive nodes", "Prior breast cancer"],
    ["Long follow-up (>12 years)", "Showed no survival effect of omitting RT in older women"],
    ["Moderate sample size (n=636)", "Many deaths from other causes limit power", "Adherence to tamoxifen not well documented"],
    "Supports omitting RT in women ≥70 with small ER+ tumours who take endocrine therapy. The key trade-off is that local recurrence is higher, and stopping endocrine therapy removes the safety net.")

add("PRIME II",
    ["Age ≥65", "HR-positive, node-negative, tumour ≤3 cm", "Clear margins (≥1 mm), on adjuvant endocrine therapy"],
    ["Grade 3 with lymphovascular invasion (both)", "HR-negative disease", "Node-positive"],
    ["Large randomised omission trial with 10-year results", "Clear absolute risk numbers for shared decisions"],
    ["Low event rate limits power for subgroups", "Endocrine adherence not verified", "Most deaths unrelated to breast cancer"],
    "Omitting RT raises 10-year local recurrence from about 1% to 9% with no survival difference. A strong basis for shared decision-making in older women, but it depends on endocrine adherence.")

add("NSABP B-39/RTOG 0413",
    ["Stage 0–II (≤3 cm, ≤3 positive nodes) after lumpectomy", "Negative margins", "Age ≥18"],
    ["Multicentric disease", "Extensive intraductal component", "Pregnancy or collagen-vascular disease"],
    ["Very large trial (n=4,216)", "Tested several APBI techniques"],
    ["APBI did not meet equivalence criteria", "Mixed risk population including higher-risk patients", "Twice-daily schedules inconvenient"],
    "Ipsilateral recurrence was only slightly higher with APBI, but the trial failed formal equivalence. It supports APBI for carefully selected low-risk women rather than broad use.")

add("IMPORT LOW",
    ["Age ≥50", "Invasive ductal carcinoma, pT1–2 (≤3 cm), pN0–1", "BCS with clear margins (≥2 mm)"],
    ["Lobular histology (in some periods)", "Neoadjuvant therapy", "Need for nodal RT"],
    ["Simple IMRT-based partial-breast technique, easy to deliver", "Non-inferiority shown with fewer adverse effects"],
    ["Low-risk population only", "Low event rates", "Requires tumour-bed clips"],
    "Partial-breast RT with standard external beam is non-inferior to whole-breast RT for low-risk women and reduces breast changes — a practical, easily adopted approach.")

add("ACOSOG Z0011",
    ["T1–2, clinically node-negative", "1–2 positive sentinel nodes", "Breast-conserving surgery with planned whole-breast RT"],
    ["Mastectomy", "Neoadjuvant therapy", "≥3 positive sentinel nodes or matted nodes"],
    ["Practice-changing de-escalation of axillary surgery", "10-year follow-up showed no survival difference"],
    ["Closed early due to poor accrual and low event rate (n=891 vs planned 1,900)", "Many had micrometastases only", "Unknown nodal RT fields — 'high tangents' were often used"],
    "Omitting axillary dissection is safe in this narrow group, but the trial was underpowered and RT fields were not controlled. It should not be extrapolated to mastectomy or neoadjuvant settings.")

add("AMAROS",
    ["T1–2, clinically node-negative", "Positive sentinel lymph node biopsy", "BCS or mastectomy"],
    ["Clinically palpable nodes", "Neoadjuvant chemotherapy", "Distant metastases"],
    ["Included mastectomy patients", "Showed less lymphoedema with axillary RT"],
    ["Low axillary event rate made non-inferiority test underpowered", "Most had low nodal burden"],
    "Axillary RT gives similar regional control with about half the lymphoedema of dissection. It is a reasonable alternative where dissection would otherwise be done.")

add("SOUND",
    ["Tumour ≤2 cm", "Negative preoperative axillary ultrasound", "Planned breast-conserving surgery + RT"],
    ["Mastectomy", "Multifocal disease", "Neoadjuvant therapy"],
    ["Tests complete omission of axillary surgery", "Non-inferior distant DFS"],
    ["Mostly postmenopausal, low-risk, HR+ patients", "Loss of nodal staging information may affect systemic therapy decisions (e.g. CDK4/6i)"],
    "Supports omitting SLNB in low-risk older women with negative ultrasound. Loss of nodal information is a real downside now that nodal status determines adjuvant abemaciclib or ribociclib.")

add("Oxford Overview (EBCTCG) chemo",
    ["Randomised trials of adjuvant polychemotherapy", "Individual patient data, >100,000 women", "Early breast cancer"],
    ["Non-randomised data"],
    ["Highest level of evidence, individual patient data", "Shows proportional benefit largely independent of age, nodal status and ER"],
    ["Older regimens dominate", "Proportional benefit does not translate into similar absolute benefit for low-risk patients", "Pre-dates genomic risk tools"],
    "Taxane-anthracycline regimens reduce breast cancer mortality by about a third. Absolute benefit depends on baseline risk, which is why genomic assays now guide chemotherapy.")

add("CALGB 9741",
    ["Node-positive operable breast cancer", "Adequate organ function", "Post surgery"],
    ["Distant metastases", "Prior chemotherapy"],
    ["2×2 factorial design tested both dose density and sequence", "Long-term follow-up"],
    ["Benefit seen mainly in ER-negative disease", "Required G-CSF support", "Older era without trastuzumab"],
    "Dose-dense every-2-week AC→T improved DFS and OS. Gains were concentrated in ER-negative tumours, so the benefit for ER-positive disease is debated.")

add("E1199",
    ["Node-positive or high-risk node-negative operable breast cancer", "After 4 cycles of AC", "Adequate organ function"],
    ["Pre-existing neuropathy", "Distant metastases"],
    ["Large 4-arm trial (n=4,950)", "Long-term follow-up"],
    ["HER2+ patients included before trastuzumab era", "Multiple comparisons"],
    "Weekly paclitaxel and 3-weekly docetaxel were superior to 3-weekly paclitaxel. Weekly paclitaxel became the preferred taxane, with particular benefit in TNBC.")

add("TAILORx",
    ["HR-positive, HER2-negative, node-negative", "Tumour 1.1–5.0 cm (or 0.6–1 cm intermediate/high grade)", "Oncotype DX recurrence score 11–25 randomised"],
    ["Node-positive disease", "HER2-positive", "Prior chemotherapy"],
    ["Very large prospective trial (n=10,273)", "Practice-changing de-escalation with 9-year follow-up"],
    ["Exploratory finding of some chemo benefit in women ≤50 with RS 16–25 (possibly ovarian suppression effect)", "Clinical risk not used for randomisation", "Non-inferiority design"],
    "Most women with RS ≤25 can skip chemotherapy. The benefit seen in younger women may reflect chemotherapy-induced ovarian suppression rather than cytotoxic effect.")

add("RxPONDER",
    ["HR-positive, HER2-negative", "1–3 positive axillary nodes", "Recurrence score ≤25"],
    ["≥4 positive nodes", "HER2-positive", "Prior chemotherapy"],
    ["Prospectively randomised in node-positive patients", "Clear menopausal interaction"],
    ["Ovarian suppression rarely used in premenopausal women", "Short follow-up for late events"],
    "Postmenopausal women with 1–3 nodes and RS ≤25 can skip chemotherapy. Premenopausal women benefited, raising the question whether ovarian suppression could substitute for chemotherapy.")

add("MINDACT",
    ["Early breast cancer, 0–3 positive nodes", "Discordant clinical (Adjuvant! Online) and genomic (MammaPrint) risk randomised"],
    ["≥4 positive nodes", "Distant metastases"],
    ["Prospective validation of a genomic signature", "Large international trial"],
    ["Primary endpoint tested only in chemo-omitted arm (single-arm comparison to threshold)", "About 1.5% absolute DMFS benefit with chemo was not ruled out", "Benefit with chemo seen in women ≤50"],
    "Supports omitting chemotherapy for high clinical/low genomic risk postmenopausal women. The small absolute benefit seen with chemotherapy in younger women needs individual discussion.")

add("ATAC",
    ["Postmenopausal women", "Invasive operable breast cancer", "Candidates for adjuvant hormonal therapy"],
    ["Prior endocrine therapy", "Metastatic disease"],
    ["Large trial with 10-year follow-up", "Established AI superiority in DFS"],
    ["No overall survival benefit", "ER-negative/unknown patients included initially", "Combination arm closed for lack of benefit"],
    "Anastrozole improved recurrence outcomes and reduced endometrial cancer and VTE versus tamoxifen, at the cost of fractures and arthralgia. OS was unchanged.")

add("ATLAS / aTTom",
    ["Women who completed ~5 years tamoxifen", "Disease-free at entry", "ER-positive (or unknown)"],
    ["Recurrence before randomisation"],
    ["Very large trials with long follow-up", "Mortality benefit seen after year 10"],
    ["Excess endometrial cancer and pulmonary embolism", "Largely pre-AI era; many patients today take AIs"],
    "Ten years of tamoxifen lowers recurrence and breast cancer mortality, with benefits emerging late. It is mainly relevant for premenopausal women who cannot take AIs.")

add("SOFT / TEXT",
    ["Premenopausal women with HR-positive early breast cancer", "Remaining premenopausal after chemotherapy (SOFT)", "Within 12 weeks of surgery (TEXT)"],
    ["HER2-positive excluded from some analyses", "Postmenopausal women"],
    ["Combined trials with >12-year follow-up", "Identified high-risk groups benefiting from OFS"],
    ["More menopausal symptoms, sexual dysfunction and bone loss", "Benefit mostly in women who needed chemotherapy and remained premenopausal", "Complex trial structure"],
    "Ovarian suppression plus exemestane improves outcomes for higher-risk premenopausal women. For low-risk women the toxicity outweighs a small gain.")

add("monarchE",
    ["HR-positive, HER2-negative, node-positive early breast cancer", "Cohort 1: ≥4 nodes, or 1–3 nodes plus grade 3 or tumour ≥5 cm", "Cohort 2: 1–3 nodes plus Ki-67 ≥20%"],
    ["Prior CDK4/6 inhibitor", "Metastatic disease", "Inflammatory breast cancer"],
    ["Large international trial with OS benefit reported", "Sustained and growing IDFS benefit"],
    ["Open-label", "Diarrhoea and neutropenia led to dose reductions in many", "Cost in low-resource settings"],
    "Two years of abemaciclib improves IDFS and now OS in high-risk node-positive disease. Cost and diarrhoea are the main barriers in India.")

add("NATALEE",
    ["HR-positive, HER2-negative stage II–III early breast cancer", "Node-negative allowed if T2 with high grade/Ki-67 or high genomic risk, or T3", "Pre- and postmenopausal"],
    ["Prior CDK4/6 inhibitor", "Metastatic disease", "QTc prolongation"],
    ["Broader population than monarchE, including high-risk N0", "Lower ribociclib dose improved tolerability"],
    ["Open-label", "OS immature", "Absolute IDFS benefit modest (about 3–5%)", "LFT and QTc monitoring needed"],
    "Extends adjuvant CDK4/6i to stage II–III disease. Modest absolute benefit, immature OS and cost make case selection important.")

add("OlympiA",
    ["Germline BRCA1/2 pathogenic variant", "HER2-negative high-risk early breast cancer", "Completed (neo)adjuvant chemotherapy"],
    ["Metastatic disease", "Prior PARP inhibitor"],
    ["OS benefit shown", "Biomarker-defined, double-blind"],
    ["Requires germline testing", "Small fraction of patients eligible", "Myelosuppression and rare MDS/AML risk"],
    "One year of olaparib improves IDFS and OS in high-risk gBRCA carriers — a strong reason to test germline BRCA in eligible patients.")

add("HERA / NSABP B-31+N9831",
    ["HER2-positive early breast cancer", "Node-positive or high-risk node-negative", "Adequate cardiac function (LVEF)"],
    ["Prior cardiac disease or low LVEF", "Metastatic disease"],
    ["Large trials with long-term OS benefit", "Established 1 year as standard duration"],
    ["Crossover in HERA diluted OS difference", "Cardiotoxicity, especially with anthracyclines", "Two years no better than one in HERA"],
    "Trastuzumab transformed HER2+ early breast cancer prognosis. Shorter durations (PERSEPHONE) remain debated, especially where cost is a barrier.")

add("APHINITY",
    ["HER2-positive operable breast cancer", "Node-positive or high-risk node-negative", "Adequate cardiac function"],
    ["Metastatic disease", "Prior anti-HER2 therapy"],
    ["Large double-blind trial", "OS signal emerging in node-positive patients"],
    ["Small absolute IDFS gain (about 2–3%)", "Benefit confined to node-positive", "More diarrhoea"],
    "Pertuzumab adds modestly to trastuzumab, mainly in node-positive disease. Its cost-effectiveness for node-negative patients is poor.")

add("APT (Tolaney)",
    ["HER2-positive, tumour ≤3 cm", "Node-negative (micrometastases allowed later)", "LVEF normal"],
    ["Node-positive disease", "Tumour >3 cm"],
    ["Defined a de-escalated, anthracycline-free regimen", "Excellent long-term outcomes"],
    ["Single-arm, no randomised comparison", "Mostly T1 tumours"],
    "Paclitaxel-trastuzumab is now standard for small node-negative HER2+ tumours. Being single-arm, it shows good outcomes but cannot prove equivalence to more intensive therapy.")

add("KATHERINE",
    ["HER2-positive early breast cancer", "Residual invasive disease after neoadjuvant taxane + trastuzumab", "Surgery completed"],
    ["Pathological complete response", "Metastatic disease", "Significant neuropathy or cardiac dysfunction"],
    ["Clear IDFS and now OS benefit", "Response-adapted strategy"],
    ["Open-label", "Neuropathy, thrombocytopenia and LFT rise", "Most patients did not receive pertuzumab neoadjuvantly"],
    "Switching to T-DM1 for residual disease cuts recurrence by about half. Its rationale supports giving neoadjuvant therapy to HER2+ tumours ≥T2 or N+.")

add("CREATE-X",
    ["HER2-negative breast cancer", "Residual invasive disease after neoadjuvant chemotherapy", "Japanese and Korean patients"],
    ["HER2-positive disease", "pCR"],
    ["DFS and OS benefit", "Cheap oral drug — very relevant in resource-limited settings"],
    ["East Asian population only", "Benefit concentrated in TNBC", "No anthracycline-taxane standard in all patients"],
    "Capecitabine improves outcomes for residual TNBC. Data in HR+ disease are weaker, and generalisability beyond East Asian patients was debated but supported by meta-analysis.")

add("KEYNOTE-522",
    ["Stage II–III triple-negative breast cancer", "ECOG PS 0–1", "Previously untreated"],
    ["Active autoimmune disease", "Systemic steroids", "Prior immunotherapy"],
    ["pCR, EFS and OS benefit", "Benefit irrespective of PD-L1"],
    ["Contribution of adjuvant pembrolizumab unclear", "Immune-related adverse events, including adrenal insufficiency", "Carboplatin added in both arms — differs from many standard regimens"],
    "Practice-changing for stage II–III TNBC. Questions remain whether all patients need adjuvant pembrolizumab, especially those with pCR.")

add("NeoSphere",
    ["HER2-positive operable, locally advanced or inflammatory breast cancer", "Tumour >2 cm", "Normal LVEF"],
    ["Metastatic disease", "Prior anti-HER2 therapy"],
    ["Randomised phase 2 showing dual blockade increases pCR", "Led to accelerated approval of neoadjuvant pertuzumab"],
    ["Phase 2, not powered for survival", "pCR used as surrogate"],
    "Established neoadjuvant pertuzumab-trastuzumab-docetaxel. The pCR advantage is real, but survival benefit relies on APHINITY rather than this trial.")

add("CTNeoBC pooled analysis",
    ["Neoadjuvant trials with individual patient data (12 trials, ~12,000 patients)", "pCR defined as ypT0/is ypN0"],
    ["Trials without long-term follow-up"],
    ["Showed patient-level association between pCR and survival, especially TNBC and HER2+", "Standardised pCR definition"],
    ["Failed to show trial-level surrogacy — pCR increases did not predict EFS gains", "Heterogeneous trials"],
    "pCR is prognostic for individuals but not a validated trial-level surrogate. This is why later trials needed EFS or OS endpoints.")

add("CLEOPATRA",
    ["HER2-positive metastatic breast cancer", "No prior chemotherapy or anti-HER2 therapy for metastatic disease", "LVEF ≥50%"],
    ["CNS metastases", "Relapse within 12 months of adjuvant trastuzumab or chemotherapy", "LVEF <50%"],
    ["Large OS benefit (median ~16 months)", "Long-term follow-up"],
    ["Few patients had prior trastuzumab", "Diarrhoea and neutropenia", "Cost"],
    "A rare trial with an unequivocal large OS benefit. Its population was mostly trastuzumab-naive, unlike most relapsing patients today.")

add("DESTINY-Breast03",
    ["HER2-positive metastatic breast cancer", "Prior trastuzumab and taxane", "Stable brain metastases allowed"],
    ["History of interstitial lung disease requiring steroids", "Active brain metastases"],
    ["Head-to-head randomised superiority over T-DM1", "Large PFS and OS benefit"],
    ["Interstitial lung disease risk", "Open-label"],
    "Defined T-DXd as second-line standard. ILD monitoring and early steroids are essential.")

add("DESTINY-Breast04",
    ["HER2-low metastatic breast cancer (IHC 1+ or 2+/ISH−)", "1–2 prior chemotherapy lines for metastatic disease", "HR+ must be endocrine refractory"],
    ["History of ILD", "Active brain metastases"],
    ["Created a new HER2-low category", "OS benefit"],
    ["HER2-low IHC scoring is poorly reproducible", "Small HR-negative cohort", "ILD risk"],
    "Practice-changing, but depends on accurate IHC; pathology quality assurance is crucial, especially for borderline 1+ cases.")

add("DESTINY-Breast06",
    ["HR-positive, HER2-low or HER2-ultralow metastatic breast cancer", "Chemotherapy-naive for metastatic disease", "Progression after ≥2 endocrine lines or within 6 months of CDK4/6i"],
    ["Prior chemotherapy for metastatic disease", "History of ILD"],
    ["Moved T-DXd ahead of chemotherapy", "Included HER2-ultralow"],
    ["OS immature", "Control chemotherapy (capecitabine, paclitaxel) arguably weak", "ILD risk"],
    "Supports T-DXd before chemotherapy, but some argue sequencing chemotherapy first could preserve T-DXd for later; OS data will decide.")

add("HER2CLIMB",
    ["HER2-positive metastatic breast cancer", "Prior trastuzumab, pertuzumab and T-DM1", "Brain metastases allowed, including untreated or progressing"],
    ["Prior lapatinib or neratinib", "Leptomeningeal disease"],
    ["Included active brain metastases — rare in trials", "OS benefit"],
    ["Diarrhoea and LFT rise", "Comparator not reflective of T-DXd era"],
    "Particularly valuable for patients with brain metastases. Place in sequencing after T-DXd is unclear.")

add("PALOMA-2",
    ["Postmenopausal HR+, HER2− advanced breast cancer", "No prior systemic therapy for advanced disease", "Measurable or bone-only disease"],
    ["Prior relapse within 12 months of adjuvant non-steroidal AI", "Visceral crisis", "CNS metastases"],
    ["Large PFS benefit", "Consistent across subgroups"],
    ["No statistically significant OS benefit", "Neutropenia frequent"],
    "Established first-line palbociclib, but unlike ribociclib and abemaciclib it never showed significant OS benefit in this setting.")

add("MONALEESA-2",
    ["Postmenopausal HR+, HER2− advanced breast cancer", "No prior therapy for advanced disease"],
    ["Prior CDK4/6 inhibitor", "Inflammatory breast cancer", "QTc prolongation"],
    ["OS benefit (~12 months)", "Long-term follow-up"],
    ["QTc and LFT monitoring needed", "Few patients with prior adjuvant AI"],
    "Supports ribociclib as preferred first-line CDK4/6 inhibitor based on OS.")

add("MONALEESA-7",
    ["Pre/perimenopausal HR+, HER2− advanced breast cancer", "No prior endocrine therapy for advanced disease (≤1 line chemo allowed)"],
    ["Prior CDK4/6 inhibitor", "QTc prolongation"],
    ["Only CDK4/6 trial dedicated to premenopausal women", "OS benefit"],
    ["Tamoxifen combination not recommended (QTc)", "Small subgroups"],
    "Key evidence for ovarian suppression plus AI plus ribociclib in young women, a large group in India.")

add("MONARCH 3",
    ["Postmenopausal HR+, HER2− advanced breast cancer", "No prior systemic therapy for advanced disease"],
    ["Prior relapse within 12 months of adjuvant NSAI", "Visceral crisis"],
    ["PFS benefit, including in poor-prognosis subgroups", "Continuous dosing"],
    ["OS benefit not statistically significant at final analysis", "Diarrhoea"],
    "Effective first-line option; the OS signal was numerically favourable but not significant.")

add("PADA-1 / SERENA-6",
    ["HR+ HER2− metastatic breast cancer on first-line AI + CDK4/6 inhibitor", "Rising ESR1 mutation in serial ctDNA without radiological progression"],
    ["Radiological progression at switch", "Prior fulvestrant/SERD"],
    ["Novel ctDNA-guided early switch strategy", "PFS improvement"],
    ["Requires serial ctDNA monitoring — costly", "OS benefit not shown", "PFS gain may partly reflect earlier detection"],
    "Proof of concept for ctDNA-guided switching. Without OS or quality-of-life gains, whether early switching beats switching at progression remains debated.")

add("SOLAR-1",
    ["HR+, HER2− advanced breast cancer", "Progression on or after AI", "PIK3CA mutation for primary cohort"],
    ["Type 1 or uncontrolled diabetes", "Prior PI3K inhibitor"],
    ["Biomarker-driven, PFS doubled in PIK3CA-mutant", "Defined PIK3CA testing"],
    ["Few patients had prior CDK4/6i", "Hyperglycaemia, rash, diarrhoea", "OS not significant"],
    "Alpelisib works in PIK3CA-mutant disease but toxicity is significant; capivasertib and inavolisib have since challenged its place.")

add("CAPItello-291",
    ["HR+, HER2− advanced breast cancer", "Progression on or after AI, with or without prior CDK4/6i", "≤2 prior endocrine lines"],
    ["Uncontrolled diabetes", "Prior AKT/PI3K/mTOR inhibitor"],
    ["Benefit in AKT-pathway-altered tumours", "Included patients after CDK4/6i"],
    ["Benefit in non-altered tumours uncertain", "Diarrhoea, rash, hyperglycaemia"],
    "Capivasertib is an option after CDK4/6i for pathway-altered tumours; biomarker testing is important.")

add("INAVO120",
    ["PIK3CA-mutated HR+, HER2− advanced breast cancer", "Endocrine-resistant: relapse during or within 12 months of adjuvant ET", "No prior therapy for advanced disease"],
    ["HbA1c ≥6.0% or diabetes requiring treatment", "Prior CDK4/6i in advanced setting"],
    ["PFS and OS benefit", "First-line triplet in high-risk group"],
    ["Narrow, endocrine-resistant population", "Hyperglycaemia and stomatitis"],
    "Establishes a first-line triplet for PIK3CA-mutant endocrine-resistant disease; requires upfront PIK3CA testing.")

add("EMERALD",
    ["ER+, HER2− advanced breast cancer", "1–2 prior endocrine lines including CDK4/6i", "≤1 prior chemotherapy line"],
    ["Visceral crisis", "Prior elacestrant or other investigational SERD", "More than one prior chemotherapy line"],
    ["First oral SERD approved", "Benefit in ESR1-mutated tumours"],
    ["Small absolute PFS gain overall", "Weak control arm (fulvestrant/AI monotherapy)", "Benefit mainly in ESR1-mutant"],
    "Elacestrant is useful for ESR1-mutated tumours. PFS gains are modest, and combinations are likely needed.")

add("OlympiAD",
    ["Germline BRCA mutation, HER2− metastatic breast cancer", "≤2 prior chemotherapy lines for metastatic disease", "Prior anthracycline and taxane"],
    ["Platinum-resistant disease", "Prior PARP inhibitor"],
    ["PFS benefit over chemotherapy", "Oral, better quality of life"],
    ["No significant OS benefit", "Control arm excluded platinum"],
    "Olaparib is a tolerable option for gBRCA carriers. The absence of a platinum comparator limits conclusions.")

add("KEYNOTE-355",
    ["Untreated locally recurrent inoperable or metastatic TNBC", "≥6 months since curative treatment", "ECOG PS 0–1"],
    ["Active autoimmune disease", "Active CNS metastases"],
    ["OS benefit in PD-L1 CPS ≥10", "Allowed different chemotherapy partners"],
    ["No benefit in CPS <10", "Biomarker cut-off derived during trial"],
    "Pembrolizumab with chemotherapy is standard for CPS ≥10 metastatic TNBC; testing PD-L1 with the correct assay is essential.")

add("ASCENT",
    ["Metastatic TNBC", "≥2 prior chemotherapy lines (one may be adjuvant if relapse ≤12 months)", "Stable brain metastases allowed (excluded from primary analysis)"],
    ["Active brain metastases in primary population", "Prior topoisomerase I inhibitor"],
    ["Large PFS and OS gains", "Benefit independent of TROP2 level"],
    ["Neutropenia and diarrhoea", "Control chemotherapy single agent"],
    "Sacituzumab is a standard later-line therapy in TNBC; manage neutropenia and diarrhoea proactively.")

add("TROPiCS-02",
    ["HR+, HER2− metastatic breast cancer", "Prior endocrine therapy, CDK4/6i and taxane", "2–4 prior chemotherapy lines"],
    ["Prior topoisomerase I inhibitor", "Active brain metastases"],
    ["OS benefit in heavily pretreated patients"],
    ["Small PFS benefit (~1.5 months)", "Toxicity in a palliative setting"],
    "OS benefit is real but modest; sequencing with T-DXd in HER2-low disease is unresolved.")
