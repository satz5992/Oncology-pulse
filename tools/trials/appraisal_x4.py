# Depth pass: breast and lung entries.
A = {}
def add(name, inc, exc, pros, cons, critique):
    A[name] = {"inclusion": inc, "exclusion": exc, "strengths": pros, "limitations": cons, "critique": critique}

add("Oxford Overview (EBCTCG) chemo",
    ["Randomised trials of adjuvant polychemotherapy vs none, or comparing regimens", "Individual patient data (~100,000 women, 123 trials)", "Early operable breast cancer"],
    ["Non-randomised or unpublished trials without individual data", "Neoadjuvant-only trials (analysed separately)"],
    ["Individual patient data — highest level of evidence", "Shows ~one-third proportional reduction in breast cancer mortality with anthracycline-taxane regimens", "Proportional benefit similar across age, nodal status and ER"],
    ["Older regimens dominate", "Same proportional benefit means small absolute gain in low-risk disease", "Pre-dates genomic risk tools and anti-HER2 therapy"],
    "The core evidence that adjuvant chemotherapy saves lives. Because the proportional effect is constant, absolute benefit depends entirely on baseline risk — the logic behind using genomic assays to spare low-risk patients.")

add("CALGB 9741",
    ["Node-positive operable breast cancer", "After mastectomy or lumpectomy with axillary dissection", "Adequate organ function"],
    ["Distant metastases", "Prior chemotherapy", "Significant cardiac disease"],
    ["2×2 factorial design tested dose density and sequence together", "Long-term follow-up showed DFS and OS benefit"],
    ["Benefit seen mainly in ER-negative tumours", "Required G-CSF support", "Pre-trastuzumab era — HER2+ patients included"],
    "Dose-dense every-2-week AC→T improved outcomes and is standard for high-risk disease. The EBCTCG dose-intensity meta-analysis later confirmed a ~10–15% proportional benefit.")

add("ATLAS / aTTom",
    ["Women who completed ~5 years of tamoxifen", "Disease-free at entry", "ER-positive (or unknown) early breast cancer"],
    ["Recurrence before randomisation", "Contraindication to continuing tamoxifen"],
    ["Very large trials (ATLAS ~12,900; aTTom ~7,000) with long follow-up", "Breast cancer mortality benefit after year 10"],
    ["Excess endometrial cancer and pulmonary embolism", "Pre-AI era; most postmenopausal women now take AIs", "ER-unknown patients in aTTom diluted effect"],
    "Ten years of tamoxifen lowers recurrence and breast cancer mortality, with benefits emerging late. It mainly guides extended therapy for premenopausal women who cannot take AIs.")

add("CTNeoBC pooled analysis",
    ["12 international neoadjuvant trials with individual patient data (~12,000 patients)", "Long-term EFS and OS available", "Standardised pCR definitions"],
    ["Trials without long-term follow-up", "Trials without individual patient data"],
    ["Showed pCR (ypT0/is ypN0) predicts better EFS and OS for individual patients", "Strongest association in TNBC and HER2+/HR− disease"],
    ["Failed to show trial-level surrogacy — increases in pCR did not predict EFS gains", "Heterogeneous trials and regimens", "Weak association in HR+/low-grade tumours"],
    "pCR is prognostic for individuals but not a validated trial-level surrogate. This is why later neoadjuvant trials (KEYNOTE-522, KATHERINE) required EFS or OS confirmation.")

add("INAVO120",
    ["PIK3CA-mutated HR+, HER2− advanced breast cancer", "Endocrine-resistant: relapse during or within 12 months of adjuvant ET", "No prior systemic therapy for advanced disease"],
    ["HbA1c ≥6.0% or diabetes requiring treatment", "Prior CDK4/6i in the advanced setting", "Symptomatic visceral crisis"],
    ["PFS and OS benefit", "First-line triplet in a high-risk, endocrine-resistant group"],
    ["Narrow population (strict glucose criteria)", "Hyperglycaemia, stomatitis and diarrhoea", "Palbociclib backbone, not ribociclib"],
    "Establishes a first-line triplet for PIK3CA-mutant endocrine-resistant disease. It requires upfront PIK3CA testing and careful glucose management.")

add("LACE meta-analysis",
    ["Completely resected NSCLC stage I–III", "Individual patient data from 5 cisplatin-based trials (n=4,584)"],
    ["Trials not cisplatin-based", "Incompletely resected patients"],
    ["Pooled individual patient data", "Defined 5.4% absolute 5-year OS benefit", "Clarified benefit by stage"],
    ["No benefit in stage IA, possible harm", "Older staging and chemotherapy partners (vinorelbine dominated)", "Many patients cannot tolerate cisplatin after lobectomy"],
    "Basis for adjuvant cisplatin doublets in stage II–III. The absolute gain is modest, which is why targeted and IO adjuvant therapies are now preferred where applicable.")

add("RTOG 0617",
    ["Unresectable stage IIIA/IIIB NSCLC", "Zubrod PS 0–1", "FEV1 ≥1.2 L"],
    ["Prior thoracic RT", "Weight loss >10%", "Supraclavicular nodes (contralateral)"],
    ["Definitive evidence that 74 Gy is harmful", "Factorial design also showed cetuximab adds nothing"],
    ["Survival deficit with high dose not fully explained", "Variation in centre experience and technique (3D vs IMRT)", "Heart dose association was exploratory"],
    "60 Gy remains standard. The trial made heart and lung dose constraints central to thoracic RT planning.")

add("CHART",
    ["Inoperable localised NSCLC", "Good performance status"],
    ["Distant metastases", "Prior thoracic RT"],
    ["Survival benefit (~9% at 2 years) from accelerated treatment", "Proof of tumour repopulation"],
    ["Three fractions daily over 12 consecutive days — logistically demanding", "No chemotherapy", "Benefit mainly in squamous histology"],
    "Showed overall treatment time matters in NSCLC, but logistics prevented adoption. Concurrent chemoRT superseded it.")

add("CHISEL",
    ["Peripheral T1–T2a N0 NSCLC, biopsy-proven", "PET-staged", "Medically inoperable or declined surgery"],
    ["Central tumours", "Prior thoracic RT"],
    ["Randomised evidence for SABR over conventional RT", "Improved local control and OS"],
    ["Small (n=101)", "Conventional arm included 50 Gy/20 fractions"],
    "Supports SABR as standard for inoperable early NSCLC, although the sample is small and some patients were treated with outdated conventional schedules.")

add("SABR-COMET",
    ["1–5 metastases, controlled primary", "ECOG PS 0–1", "Life expectancy ≥6 months"],
    ["Brain metastases >3 cm", "Malignant pleural effusion", "Spinal cord compression"],
    ["OS benefit in randomised phase 2", "Long-term follow-up (8 years)"],
    ["Small (n=99), mixed histology", "Treatment-related deaths (~4.5%)", "Imbalance favouring prostate primaries in SABR arm"],
    "Hypothesis-generating rather than definitive. Phase 3 trials (SABR-COMET-3, -10) are needed before widespread use.")

add("FLAURA",
    ["Advanced NSCLC with EGFR exon 19 deletion or L858R", "Treatment-naive for advanced disease", "Stable CNS metastases allowed"],
    ["Prior EGFR TKI", "History of ILD", "QTc prolongation"],
    ["PFS (18.9 vs 10.2 months) and OS benefit", "Better CNS efficacy"],
    ["OS benefit not seen in Asian subgroup", "Comparator first-generation TKIs; many control patients never received osimertinib"],
    "Osimertinib became first-line standard. The Asian subgroup result and the fact that not all controls crossed over to osimertinib are the main criticisms.")

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
    "Alectinib became first-line standard for ALK+ NSCLC. Lorlatinib (CROWN) now challenges it for patients who can tolerate CNS side effects.")

add("CROWN",
    ["Advanced ALK-positive NSCLC", "Treatment-naive", "Asymptomatic CNS metastases allowed"],
    ["Prior ALK inhibitor", "Spinal cord compression"],
    ["5-year PFS ~60% — unprecedented", "Excellent CNS control"],
    ["Comparator crizotinib", "Neurocognitive and mood effects, weight gain, hyperlipidaemia"],
    "Lorlatinib offers the longest PFS; neurocognitive toxicity and lipid monitoring are key, and patient preference matters.")

add("KEYNOTE-189",
    ["Advanced non-squamous NSCLC", "No EGFR/ALK alterations", "Treatment-naive"],
    ["Active autoimmune disease", "Untreated CNS metastases", "Pneumonitis needing steroids"],
    ["OS benefit across PD-L1 strata", "Long-term follow-up shows durable responses"],
    ["Smaller benefit in PD-L1 <1%", "Nephritis and immune toxicity"],
    "Chemo-pembrolizumab is the standard for non-squamous NSCLC regardless of PD-L1. In PD-L1 ≥50%, pembrolizumab alone may suffice.")

add("KEYNOTE-407",
    ["Advanced squamous NSCLC", "Treatment-naive", "ECOG PS 0–1"],
    ["Active autoimmune disease", "Untreated CNS metastases"],
    ["OS benefit across PD-L1 levels", "Carboplatin with paclitaxel or nab-paclitaxel"],
    ["Smaller benefit in PD-L1 <1%", "Neuropathy and myelosuppression"],
    "Chemo-pembrolizumab is standard for squamous NSCLC. It was the first IO trial to show OS benefit in this histology.")

add("CheckMate 9LA",
    ["Advanced NSCLC (squamous or non-squamous)", "No EGFR/ALK alterations", "Treatment-naive"],
    ["Active autoimmune disease", "Untreated CNS metastases"],
    ["OS benefit, especially in squamous and PD-L1 <1%", "Only 2 cycles of chemotherapy"],
    ["Higher immune toxicity from ipilimumab", "No direct comparison with chemo-pembrolizumab"],
    "An option for PD-L1-negative or squamous disease; toxicity is a trade-off.")

add("PARAMOUNT",
    ["Advanced non-squamous NSCLC", "No progression after 4 cycles of cisplatin-pemetrexed", "ECOG PS 0–1"],
    ["Squamous histology", "Progression during induction"],
    ["OS benefit for continuation maintenance", "Well tolerated"],
    ["Pre-immunotherapy era", "Selected patients who completed induction"],
    "Established pemetrexed maintenance, now incorporated into chemo-IO regimens like KEYNOTE-189.")

add("Scagliotti cis-pem vs cis-gem",
    ["Advanced NSCLC, chemotherapy-naive", "ECOG PS 0–1"],
    ["Prior chemotherapy", "Symptomatic brain metastases"],
    ["Revealed histology as a predictive factor", "Large trial (n=1,725)"],
    ["Non-inferiority design; histology finding was a pre-planned subgroup", "Pre-molecular era"],
    "Made histology essential for chemotherapy choice — pemetrexed for non-squamous, gemcitabine for squamous.")

add("Temel early palliative care",
    ["Newly diagnosed metastatic NSCLC", "ECOG PS 0–2", "Within 8 weeks of diagnosis"],
    ["Already receiving palliative care", "Unable to complete questionnaires"],
    ["Improved quality of life and mood", "Longer survival despite less aggressive end-of-life care"],
    ["Single centre, small (n=151)", "Survival endpoint secondary", "Not blinded"],
    "Strong case for early integrated palliative care. Generalisability to resource-limited settings needs local models.")

add("CodeBreaK 200",
    ["KRAS G12C-mutant advanced NSCLC", "Progression after platinum chemotherapy and checkpoint inhibitor"],
    ["Active brain metastases", "Prior KRAS G12C inhibitor or docetaxel"],
    ["First randomised phase 3 of a KRAS G12C inhibitor", "Better tolerability than docetaxel"],
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
    "Led to accelerated approval; randomised data are pending. ILD monitoring is essential.")

add("CONVERT",
    ["Limited-stage SCLC", "ECOG PS 0–2"],
    ["Prior thoracic RT", "Pleural effusion"],
    ["Modern 3D-conformal or IMRT", "Showed similar OS between schedules"],
    ["Designed for superiority of once daily — failed", "Underpowered for equivalence"],
    "Twice-daily 45 Gy remains standard, but 66 Gy once daily is acceptable when BID is impractical.")

add("Turrisi INT 0096",
    ["Limited-stage SCLC", "Good performance status"],
    ["Pleural effusion", "Prior thoracic RT"],
    ["Showed accelerated BID RT improves survival", "Long-term follow-up"],
    ["Once-daily arm only 45 Gy — low dose", "Higher oesophagitis with BID"],
    "Basis for 45 Gy BID. The low once-daily dose made the comparison unfair, prompting CONVERT and CALGB 30610.")

add("Aupérin PCI meta-analysis",
    ["SCLC in complete remission after induction", "Individual patient data from 7 trials"],
    ["Patients without complete response", "Brain metastases at diagnosis"],
    ["Showed OS benefit (~5% at 3 years)", "Reduced brain metastasis incidence"],
    ["Mostly limited-stage; brain imaging not mandatory", "Pre-MRI era"],
    "PCI benefits patients with complete response, but with MRI surveillance the case for PCI is being re-examined (Japanese ES-SCLC trial).")

add("ADRIATIC",
    ["Limited-stage SCLC", "No progression after concurrent platinum-etoposide chemoRT", "PCI allowed"],
    ["Prior immunotherapy", "Grade ≥2 pneumonitis"],
    ["OS and PFS benefit — first major LS-SCLC advance in decades", "Double-blind"],
    ["Randomisation after chemoRT selects responders", "Pneumonitis risk"],
    "Durvalumab consolidation is a new standard in LS-SCLC.")

add("IMpower133",
    ["Treatment-naive ES-SCLC", "ECOG PS 0–1", "Treated asymptomatic brain metastases allowed"],
    ["Active autoimmune disease", "Untreated brain metastases"],
    ["OS benefit", "Double-blind"],
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
    ["OS benefit over standard chemotherapy", "Better tolerability than chemotherapy"],
    ["Cytokine release syndrome and neurotoxicity", "Requires inpatient monitoring for first doses"],
    "Tarlatamab is a new second-line standard; logistics of CRS monitoring matter.")
