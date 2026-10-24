# Full-depth rewrites (overrides earlier entries). Breast leftovers + lung.
A = {}
def add(name, inc, exc, pros, cons, critique):
    A[name] = {"inclusion": inc, "exclusion": exc, "strengths": pros, "limitations": cons, "critique": critique}

add("DESTINY-Breast03",
    ["HER2-positive unresectable or metastatic breast cancer", "Progression after trastuzumab and a taxane (advanced or within 6 months of (neo)adjuvant therapy)", "Clinically stable, treated brain metastases allowed"],
    ["History of non-infectious ILD/pneumonitis requiring steroids, or current ILD", "Symptomatic or untreated brain metastases", "Prior T-DM1 for metastatic disease"],
    ["Randomised head-to-head superiority over the previous second-line standard", "Very large PFS benefit (HR ~0.33) and later OS benefit", "Consistent benefit including stable brain metastases"],
    ["Open-label design", "Drug-related ILD in about 15% (mostly grade 1–2, rare deaths)", "Few patients had prior pertuzumab-free first line, so applicability to pertuzumab-naive Indian patients is uncertain"],
    "T-DXd became the second-line standard for HER2+ MBC. Benefit is unquestioned; the practical issues are ILD surveillance (baseline CT, early steroids) and cost, and its sequencing relative to tucatinib in patients with brain metastases.")

add("HER2CLIMB",
    ["HER2-positive metastatic breast cancer", "Prior trastuzumab, pertuzumab and T-DM1", "Brain metastases allowed, including untreated or progressing after local therapy"],
    ["Prior lapatinib (within 12 months) or neratinib, tucatinib or other HER2 TKIs", "Leptomeningeal disease", "Brain lesions needing immediate local therapy"],
    ["Included patients with active brain metastases — usually excluded from trials", "OS benefit overall and in the brain-metastasis subgroup", "Oral TKI with good CNS activity"],
    ["Comparator (trastuzumab-capecitabine) pre-dates T-DXd", "Diarrhoea, hand-foot syndrome and LFT rise", "Benefit after T-DXd not tested in the trial"],
    "Tucatinib-trastuzumab-capecitabine is the regimen of choice when brain metastases dominate. In the T-DXd era its place is usually third line or for CNS progression.")

add("MONALEESA-2",
    ["Postmenopausal women with HR+, HER2− recurrent or metastatic breast cancer", "No prior systemic therapy for advanced disease", "Measurable disease or ≥1 lytic bone lesion"],
    ["Prior CDK4/6 inhibitor", "Relapse during or within 12 months of (neo)adjuvant NSAI", "QTcF >450 ms or significant cardiac disease; inflammatory breast cancer; CNS metastases"],
    ["Double-blind, placebo-controlled", "Statistically significant OS benefit (~12 months median) with long follow-up", "Consistent benefit across subgroups including visceral disease"],
    ["Mostly endocrine-sensitive patients — few had relapsed early on adjuvant ET", "QTc prolongation, hepatotoxicity and neutropenia require monitoring", "Postmenopausal only"],
    "Ribociclib with letrozole is a preferred first-line option because of proven OS. ECG and LFT monitoring in the first months is mandatory, and drug interactions affecting QTc must be checked.")

add("MONALEESA-7",
    ["Pre- or perimenopausal women, HR+, HER2− advanced breast cancer", "No prior endocrine therapy for advanced disease; ≤1 prior chemotherapy line allowed", "Ovarian suppression with goserelin"],
    ["Prior CDK4/6 inhibitor", "QTc prolongation or significant cardiac disease", "CNS metastases"],
    ["Only phase 3 CDK4/6 trial dedicated to premenopausal women", "OS benefit", "Allowed one prior line of chemotherapy, reflecting real practice"],
    ["Tamoxifen combination raised QTc and is not recommended", "Requires continuous ovarian suppression", "Moderate sample size for subgroup analysis"],
    "Key evidence for OFS + NSAI + ribociclib in young women with metastatic HR+ disease — a large group in India where breast cancer presents younger.")

add("MONARCH 3",
    ["Postmenopausal women, HR+, HER2− advanced breast cancer", "No prior systemic therapy for advanced disease", "Measurable or non-measurable bone-only disease"],
    ["Relapse within 12 months of adjuvant NSAI", "Visceral crisis", "CNS metastases"],
    ["Double-blind; large PFS gain", "Continuous dosing schedule", "Benefit also in poor-prognosis groups (liver metastases, short treatment-free interval)"],
    ["Final OS benefit numerically ~13 months but not statistically significant", "Diarrhoea frequent early", "VTE and transaminase elevation"],
    "Effective first-line partner for AIs. Lack of a significant OS result (unlike MONALEESA-2) has led many guidelines to favour ribociclib, although cross-trial comparison is limited.")

add("CAPItello-291",
    ["HR+, HER2− advanced breast cancer", "Relapse or progression on or after AI-based treatment (CDK4/6i allowed, ~70% had it)", "≤2 prior endocrine lines and ≤1 chemotherapy line for advanced disease"],
    ["Uncontrolled diabetes (HbA1c ≥8%)", "Prior AKT, PI3K or mTOR inhibitor, SERD or fulvestrant", "Symptomatic visceral disease"],
    ["Dual primary endpoint in overall and AKT-pathway-altered populations", "Includes the post-CDK4/6 population seen in practice"],
    ["Exploratory data suggest little benefit when PIK3CA/AKT1/PTEN are not altered", "Diarrhoea, rash and hyperglycaemia", "Modest absolute PFS gain"],
    "Capivasertib plus fulvestrant is a second-line option for pathway-altered tumours. Testing (tissue or ctDNA) should guide use rather than giving it to all-comers.")

add("EMERALD",
    ["ER+, HER2− advanced breast cancer, men and postmenopausal women", "1–2 prior endocrine lines including a CDK4/6 inhibitor", "≤1 prior chemotherapy line"],
    ["Prior elacestrant or other investigational SERD", "Symptomatic visceral disease or visceral crisis", "More than one prior chemotherapy line"],
    ["First oral SERD to show benefit in phase 3", "Prespecified ESR1-mutated analysis"],
    ["Overall PFS gain small; benefit concentrated in ESR1-mutated tumours", "Control arm was endocrine monotherapy (fulvestrant or AI), a weak comparator", "Nausea"],
    "Elacestrant is reasonable for ESR1-mutated disease after CDK4/6i, especially when endocrine sensitivity was long (≥12 months on prior CDK4/6i). Combination strategies are likely to supersede monotherapy.")

add("OlympiAD",
    ["Germline BRCA1/2 mutation, HER2-negative metastatic breast cancer", "≤2 prior chemotherapy lines for metastatic disease", "Prior anthracycline and taxane; HR+ must have had endocrine therapy"],
    ["Progression on platinum for advanced disease", "Prior PARP inhibitor", "MDS/AML features"],
    ["Oral targeted therapy with better quality of life than chemotherapy", "PFS benefit (7.0 vs 4.2 months)"],
    ["No significant OS benefit overall (possible benefit in first line)", "Platinum excluded from control arm", "Open-label"],
    "Olaparib is a tolerable option in gBRCA MBC, but the absence of a platinum comparator means its superiority over carboplatin is unproven.")

add("ASCENT",
    ["Metastatic TNBC", "≥2 prior systemic chemotherapy regimens (one could be adjuvant if relapse within 12 months)", "Stable treated brain metastases allowed (excluded from primary analysis)"],
    ["Prior topoisomerase-1 inhibitor", "Active or unstable brain metastases (for primary analysis)", "Bulky disease affecting organ function"],
    ["Large PFS and OS benefit (median OS ~12 vs 6.7 months)", "Benefit seen across TROP2 expression levels"],
    ["Neutropenia and diarrhoea are common; G-CSF often needed", "Single-agent chemotherapy control"],
    "Sacituzumab is a standard later-line therapy in TNBC. UGT1A1*28 homozygotes have more toxicity, and supportive care planning is important.")

add("TROPiCS-02",
    ["HR+, HER2− metastatic breast cancer", "Prior endocrine therapy, CDK4/6 inhibitor and taxane", "2–4 prior chemotherapy lines for metastatic disease"],
    ["Prior topoisomerase-1 inhibitor", "Active CNS metastases"],
    ["OS benefit in a heavily pretreated population", "Better quality of life measures"],
    ["Small PFS gain (~1.5 months)", "Neutropenia and diarrhoea", "Sequencing with T-DXd untested"],
    "OS gain (~3 months) is modest but real. In HER2-low disease, most clinicians use T-DXd first; sequential ADC benefit appears smaller.")

# Lung
add("ALINA",
    ["Completely resected stage IB (≥4 cm)–IIIA NSCLC (7th ed.)", "ALK rearrangement", "ECOG PS 0–1"],
    ["Prior systemic therapy or RT for lung cancer", "Incomplete resection"],
    ["Direct comparison with standard adjuvant chemotherapy", "Very large DFS benefit (HR ~0.24) including CNS DFS"],
    ["OS immature", "2-year duration arbitrary", "Open-label"],
    "Alectinib replaced adjuvant chemotherapy for resected ALK+ NSCLC. Whether it cures or delays relapse will be answered only by OS.")

add("KEYNOTE-671",
    ["Resectable stage II–IIIB (N2) NSCLC (8th ed.)", "ECOG PS 0–1", "No prior treatment"],
    ["Known EGFR/ALK alterations (few included)", "Active autoimmune disease"],
    ["EFS and OS benefit — first perioperative IO trial with OS", "Large international trial"],
    ["Cannot separate neoadjuvant from adjuvant contribution", "Some patients did not reach surgery", "Adjuvant phase adds a year of toxicity and cost"],
    "Perioperative pembrolizumab is a standard. Whether patients with pCR need adjuvant therapy is unresolved; neoadjuvant-only (CheckMate 816) is an alternative.")

add("LAURA",
    ["Unresectable stage III NSCLC", "EGFR exon 19 deletion or L858R", "No progression after definitive concurrent or sequential platinum chemoRT"],
    ["Prior EGFR TKI", "Symptomatic pneumonitis after chemoRT"],
    ["Very large PFS benefit (HR ~0.16)", "Addresses EGFR-mutant patients who gain little from durvalumab"],
    ["OS immature with high crossover", "Treatment until progression — duration and cost uncertain"],
    "Osimertinib consolidation is standard for EGFR-mutant stage III. Whether early vs at-progression osimertinib improves OS remains open.")

add("RTOG 9410",
    ["Unresectable stage II–IIIB NSCLC", "KPS ≥70", "Weight loss <5%"],
    ["Pleural effusion", "Prior thoracic RT or chemotherapy"],
    ["Showed concurrent chemoRT improves OS over sequential", "Long-term follow-up"],
    ["Old 2D RT and chemotherapy (cisplatin-vinblastine)", "Higher acute oesophagitis with concurrent therapy", "BID arm offered no further gain"],
    "Basis for concurrent chemoRT in fit patients. Sequential remains reasonable for frail or large-volume patients where toxicity is prohibitive.")

add("RTOG 0617",
    ["Unresectable stage IIIA/IIIB NSCLC", "Zubrod PS 0–1", "FEV1 ≥1.2 L"],
    ["Prior thoracic RT", "Supraclavicular nodes in some protocols", "Weight loss >10%"],
    ["Definitive evidence that 74 Gy is harmful", "Factorial design also showed cetuximab adds nothing"],
    ["Survival deficit with high dose not fully explained", "Variation in centre experience and RT technique (3D vs IMRT)", "Heart dose association was exploratory"],
    "60 Gy remains standard. The trial made heart and lung dose constraints central to thoracic RT planning.")

add("CHART",
    ["Inoperable localised NSCLC", "Good performance status"],
    ["Distant metastases", "Prior RT"],
    ["Survival benefit (~9% at 2 years) from accelerated treatment", "Proof of tumour repopulation"],
    ["Three fractions daily over 12 consecutive days — logistically demanding", "No chemotherapy", "Benefit mainly in squamous histology"],
    "Showed overall treatment time matters, but logistics prevented adoption. Concurrent chemoRT superseded it.")

add("CHISEL",
    ["Peripheral T1–T2a N0 NSCLC, biopsy-proven", "PET-staged", "Medically inoperable or declined surgery"],
    ["Central tumours", "Prior thoracic RT"],
    ["Randomised evidence for SABR over conventional RT", "Improved local control and OS"],
    ["Small (n=101)", "Conventional arm included 50 Gy/20 fractions"],
    "Supports SABR as standard for inoperable early NSCLC, although the sample is small.")

add("IPASS",
    ["East Asian patients with stage IIIB/IV adenocarcinoma", "Never or light former smokers", "Chemotherapy-naive"],
    ["Prior chemotherapy or biological therapy", "Unstable brain metastases"],
    ["Showed EGFR mutation as predictive biomarker", "Paved way for molecular testing"],
    ["Clinical rather than molecular selection", "OS not different because of crossover"],
    "Gefitinib was better only in EGFR-mutant tumours and worse in wild-type, making EGFR testing mandatory before first-line therapy.")

add("FLAURA",
    ["Advanced NSCLC with EGFR exon 19 deletion or L858R", "Treatment-naive for advanced disease", "Stable CNS metastases allowed"],
    ["Prior EGFR TKI", "History of ILD", "QTc prolongation"],
    ["PFS (18.9 vs 10.2 months) and OS benefit", "Better CNS efficacy"],
    ["OS benefit not seen in Asian subgroup", "Comparator first-generation TKIs; many control patients never received osimertinib"],
    "Osimertinib became first-line standard. The Asian subgroup result and comparator choice are the main criticisms.")

add("FLAURA2",
    ["Advanced EGFR-mutant (ex19del/L858R) non-squamous NSCLC", "Treatment-naive", "ECOG PS 0–1"],
    ["Prior EGFR TKI", "History of ILD"],
    ["PFS benefit and OS benefit", "Greater benefit in CNS metastases and L858R"],
    ["More chemotherapy toxicity and time in clinic", "Unclear who needs intensification upfront"],
    "Adding chemotherapy to osimertinib helps, but at a toxicity cost. It is best for higher-risk patients (CNS metastases, L858R, TP53 co-mutation, high ctDNA).")

add("MARIPOSA",
    ["Advanced EGFR-mutant (ex19del/L858R) NSCLC", "Treatment-naive", "ECOG PS 0–1"],
    ["Prior EGFR TKI", "History of ILD", "Untreated brain metastases"],
    ["PFS and OS benefit over osimertinib"],
    ["IV amivantamab with infusion reactions, rash, paronychia and VTE", "Prophylactic anticoagulation needed", "Cost and chair time"],
    "Effective combination, but toxicity and logistics limit uptake, especially in resource-limited settings. A subcutaneous formulation may help.")

add("ALEX",
    ["Advanced ALK-positive NSCLC", "Treatment-naive", "Asymptomatic CNS metastases allowed"],
    ["Prior ALK inhibitor", "Symptomatic CNS metastases"],
    ["Large PFS benefit (~35 vs 11 months)", "Superior CNS protection"],
    ["Comparator crizotinib has weak CNS penetration", "OS data immature for years"],
    "Alectinib became first-line standard for ALK+ NSCLC.")

add("CROWN",
    ["Advanced ALK-positive NSCLC", "Treatment-naive", "Asymptomatic CNS metastases allowed"],
    ["Prior ALK inhibitor", "Spinal cord compression"],
    ["5-year PFS ~60% — unprecedented", "Excellent CNS control"],
    ["Comparator crizotinib", "Neurocognitive and mood effects, weight gain, hyperlipidaemia"],
    "Lorlatinib offers the longest PFS; neurocognitive toxicity and lipid monitoring are key.")

add("KEYNOTE-189",
    ["Advanced non-squamous NSCLC", "No EGFR/ALK alterations", "Treatment-naive"],
    ["Active autoimmune disease", "Untreated CNS metastases", "Pneumonitis needing steroids"],
    ["OS benefit across PD-L1 strata", "Long-term follow-up shows durable responses"],
    ["Smaller benefit in PD-L1 <1%", "Nephritis and immune toxicity"],
    "Chemo-pembrolizumab is the standard for non-squamous NSCLC regardless of PD-L1.")

add("KEYNOTE-407",
    ["Advanced squamous NSCLC", "Treatment-naive", "ECOG PS 0–1"],
    ["Active autoimmune disease", "Untreated CNS metastases"],
    ["OS benefit across PD-L1 levels", "Carboplatin with paclitaxel or nab-paclitaxel"],
    ["Smaller benefit in PD-L1 <1%"],
    "Chemo-pembrolizumab is standard for squamous NSCLC.")

add("CheckMate 9LA",
    ["Advanced NSCLC (squamous or non-squamous)", "No EGFR/ALK alterations", "Treatment-naive"],
    ["Active autoimmune disease", "Untreated CNS metastases"],
    ["OS benefit, especially in squamous and PD-L1 <1%", "Only 2 cycles of chemotherapy"],
    ["Higher immune toxicity from ipilimumab", "No direct comparison with chemo-pembrolizumab"],
    "An option for PD-L1-negative or squamous disease; toxicity is a trade-off.")

add("PARAMOUNT",
    ["Advanced non-squamous NSCLC", "No progression after 4 cycles of cisplatin-pemetrexed", "ECOG PS 0–1"],
    ["Squamous histology", "Progression during induction"],
    ["OS benefit for continuation maintenance"],
    ["Pre-immunotherapy era", "Selected patients who completed induction"],
    "Established pemetrexed maintenance, now incorporated into chemo-IO regimens.")

add("Scagliotti cis-pem vs cis-gem",
    ["Advanced NSCLC, chemotherapy-naive", "ECOG PS 0–1"],
    ["Prior chemotherapy", "Symptomatic brain metastases"],
    ["Revealed histology as a predictive factor", "Large trial (n=1,725)"],
    ["Non-inferiority design; histology finding was a pre-planned subgroup"],
    "Made histology essential for chemotherapy choice — pemetrexed for non-squamous, gemcitabine for squamous.")

add("CodeBreaK 200",
    ["KRAS G12C-mutant advanced NSCLC", "Progression after platinum chemotherapy and checkpoint inhibitor"],
    ["Active brain metastases", "Prior KRAS G12C inhibitor or docetaxel"],
    ["First randomised phase 3 of a KRAS G12C inhibitor"],
    ["Modest PFS gain (5.6 vs 4.5 months), no OS benefit", "Crossover and early dropouts in docetaxel arm", "FDA raised concerns about assessment bias"],
    "Sotorasib is modestly better than docetaxel. The modest gain and bias concerns led to scepticism and a withheld full approval.")

add("LIBRETTO-431",
    ["RET fusion-positive advanced non-squamous NSCLC", "Treatment-naive"],
    ["Prior systemic therapy for advanced disease", "Symptomatic CNS metastases"],
    ["Large PFS benefit over chemo-pembrolizumab", "Strong CNS activity"],
    ["Rare population", "OS immature"],
    "Supports first-line selpercatinib and broad NGS panels at diagnosis.")

add("DESTINY-Lung01/02",
    ["HER2 (ERBB2)-mutant advanced NSCLC", "Prior systemic therapy"],
    ["History of ILD", "Untreated brain metastases"],
    ["High response rates (~50%)", "Lower dose (5.4 mg/kg) reduced ILD"],
    ["Non-randomised", "ILD risk"],
    "Led to accelerated approval; randomised data are pending.")

add("CONVERT",
    ["Limited-stage SCLC", "ECOG PS 0–2"],
    ["Prior thoracic RT", "Pleural effusion"],
    ["Modern 3D-conformal or IMRT", "Showed similar OS between schedules"],
    ["Designed for superiority of once daily — failed", "Underpowered for equivalence"],
    "Twice-daily 45 Gy remains standard, but 66 Gy once daily is acceptable when BID is impractical.")

add("Turrisi INT 0096",
    ["Limited-stage SCLC", "Good performance status"],
    ["Pleural effusion", "Prior thoracic RT"],
    ["Showed accelerated BID RT improves survival"],
    ["Once-daily arm only 45 Gy — low dose", "Higher oesophagitis with BID"],
    "Basis for 45 Gy BID. The low once-daily dose made the comparison unfair, prompting CONVERT and CALGB 30610.")

add("ADRIATIC",
    ["Limited-stage SCLC", "No progression after concurrent platinum-etoposide chemoRT", "PCI allowed"],
    ["Prior immunotherapy", "Grade ≥2 pneumonitis"],
    ["OS and PFS benefit — first major LS-SCLC advance in decades"],
    ["Randomisation after chemoRT selects responders", "Pneumonitis risk"],
    "Durvalumab consolidation is a new standard in LS-SCLC.")

add("IMpower133",
    ["Treatment-naive ES-SCLC", "ECOG PS 0–1", "Treated asymptomatic brain metastases allowed"],
    ["Active autoimmune disease", "Untreated brain metastases"],
    ["OS benefit"],
    ["Modest median OS gain (~2 months)", "Only 4 cycles of chemotherapy"],
    "Small but real OS benefit; a minority are long-term survivors.")

add("CASPIAN",
    ["Treatment-naive ES-SCLC", "WHO PS 0–1", "Asymptomatic or treated brain metastases allowed"],
    ["Prior immunotherapy", "Active autoimmune disease"],
    ["OS benefit", "Allowed cisplatin or carboplatin and up to 4 cycles"],
    ["Modest benefit (~2–3 months median)", "PCI not allowed in IO arm"],
    "Confirms chemo-IO as first-line standard in ES-SCLC.")

add("CREST (Slotman)",
    ["ES-SCLC with response to 4–6 cycles chemotherapy", "WHO PS 0–2"],
    ["Brain or leptomeningeal metastases", "Progressive disease"],
    ["Improved 2-year OS and intrathoracic control"],
    ["Primary 1-year OS endpoint not met", "Pre-immunotherapy era", "30 Gy/10 fractions — low dose"],
    "Supports consolidative thoracic RT in responders with residual thoracic disease; its role with IO is under study.")

add("DeLLphi-304",
    ["SCLC progressing after first-line platinum chemotherapy (± immunotherapy)", "ECOG PS 0–1", "Treated, stable brain metastases allowed"],
    ["Prior DLL3-targeted therapy", "Symptomatic CNS metastases"],
    ["OS benefit over standard chemotherapy"],
    ["Cytokine release syndrome and neurotoxicity", "Requires inpatient monitoring for first doses"],
    "Tarlatamab is a new second-line standard; logistics of CRS monitoring matter.")
