# Critical appraisal for lung trials. Revision aid; verify against the primary paper.
A = {}
def add(name, inc, exc, pros, cons, critique):
    A[name] = {"inclusion": inc, "exclusion": exc, "strengths": pros, "limitations": cons, "critique": critique}

add("NLST",
    ["Age 55–74", "≥30 pack-years", "Current smoker or quit within 15 years"],
    ["Prior lung cancer", "Chest CT within 18 months", "Symptoms suggesting lung cancer (haemoptysis, weight loss)"],
    ["Very large RCT (n=53,454) with lung cancer mortality endpoint", "Led to screening guidelines"],
    ["Chest X-ray comparator rather than no screening", "High false-positive rate (~24% per round)", "Volunteers healthier and better educated than general smokers"],
    "First RCT to show screening saves lives (20% relative reduction in lung cancer mortality). False positives, overdiagnosis and an older US population limit direct transfer to India, where TB-related nodules are common.")

add("NELSON",
    ["Age 50–74", "Heavy smokers (>15 cigarettes/day for >25 years or >10/day for >30 years)", "Current or quit ≤10 years"],
    ["Poor self-reported health", "Recent chest CT"],
    ["Volume-based nodule management cut false positives", "No-screening control arm", "Mortality benefit larger in women"],
    ["Mostly men", "Only 4 screening rounds", "Smaller sample than NLST"],
    "Confirmed NLST with fewer false positives through volumetric protocols. The structured nodule management is as important as the CT itself.")

add("LACE meta-analysis",
    ["Completely resected NSCLC stage I–III", "Individual patient data from 5 cisplatin trials (n=4,584)"],
    ["Trials not cisplatin-based"],
    ["Pooled individual patient data", "Defined 5% absolute 5-year OS benefit"],
    ["No benefit in stage IA, possible harm in IA", "Older staging and chemotherapy partners (vinorelbine dominated)"],
    "Basis for adjuvant cisplatin doublets in stage II–III. The absolute gain is modest, and many patients cannot tolerate cisplatin after lobectomy.")

add("ADAURA",
    ["Completely resected stage IB–IIIA (7th ed.) non-squamous NSCLC", "EGFR exon 19 deletion or L858R", "Adjuvant chemotherapy allowed but not required"],
    ["Prior EGFR TKI", "Interstitial lung disease", "Incomplete resection"],
    ["Large DFS benefit and later OS benefit", "Reduced CNS recurrence"],
    ["Placebo control — no comparison with osimertinib at relapse for all", "PET and brain MRI staging not required", "Optimal duration (3 years) untested"],
    "Osimertinib improved OS, settling much debate, though some argue part of the effect reflects deferral rather than cure. Mandatory EGFR testing in resected non-squamous NSCLC follows.")

add("ALINA",
    ["Completely resected stage IB (≥4 cm)–IIIA ALK-positive NSCLC", "ECOG PS 0–1"],
    ["Prior systemic therapy", "Incomplete resection"],
    ["Large DFS benefit including CNS", "Direct comparison with chemotherapy"],
    ["OS immature", "Duration of 2 years arbitrary"],
    "Alectinib replaced adjuvant chemotherapy for resected ALK+ NSCLC; OS confirmation awaited.")

add("CheckMate 816",
    ["Resectable stage IB (≥4 cm)–IIIA NSCLC (7th ed.)", "ECOG PS 0–1", "No known EGFR/ALK alterations"],
    ["Known EGFR mutation or ALK translocation", "Active autoimmune disease"],
    ["Improved EFS and pCR with only 3 cycles", "No increase in surgical complications"],
    ["No adjuvant phase — optimal total duration unclear", "Benefit mainly PD-L1 ≥1%", "OS data later"],
    "Neoadjuvant chemo-IO is standard for resectable NSCLC. Debate continues over neoadjuvant-only vs perioperative approaches.")

add("KEYNOTE-671",
    ["Resectable stage II–IIIB (N2) NSCLC", "ECOG PS 0–1"],
    ["Prior therapy for lung cancer", "Known EGFR/ALK (allowed but few)"],
    ["EFS and OS benefit", "Perioperative design"],
    ["Contribution of adjuvant phase unknown", "Toxicity of a year of pembrolizumab"],
    "First perioperative IO trial with OS benefit; whether adjuvant pembrolizumab is needed after pCR remains open.")

add("PACIFIC",
    ["Unresectable stage III NSCLC", "No progression after ≥2 cycles platinum concurrent chemoRT", "ECOG PS 0–1"],
    ["Prior immunotherapy", "Grade ≥2 pneumonitis from chemoRT", "Active autoimmune disease"],
    ["Large OS benefit with 5-year follow-up", "Changed standard of care"],
    ["Randomised after chemoRT, so excluded patients who progressed", "Post-hoc data suggest little benefit if PD-L1 <1%", "EGFR-mutant patients do not benefit"],
    "Durvalumab consolidation is standard after concurrent chemoRT. The selected population (fit, non-progressing) and limited benefit in PD-L1-negative and EGFR-mutant disease are key caveats.")

add("LAURA",
    ["Unresectable stage III EGFR-mutant NSCLC", "No progression after definitive chemoRT"],
    ["Prior EGFR TKI", "Interstitial lung disease"],
    ["Very large PFS benefit", "Addresses population not helped by durvalumab"],
    ["OS immature with high crossover", "Indefinite treatment duration"],
    "Osimertinib after chemoRT is standard in EGFR-mutant stage III; the cost of indefinite therapy is a concern.")

add("RTOG 9410",
    ["Unresectable stage II–III NSCLC", "KPS ≥70", "Weight loss <5%"],
    ["Pleural effusion", "Prior thoracic RT"],
    ["Showed concurrent superior to sequential chemoRT", "Long-term follow-up"],
    ["Older RT technique and chemotherapy", "Higher oesophagitis with concurrent therapy"],
    "Basis for concurrent cisplatin-based chemoRT in fit patients; sequential therapy remains reasonable in frail patients.")

add("RTOG 0617",
    ["Unresectable stage IIIA/IIIB NSCLC", "Zubrod PS 0–1", "FEV1 ≥1.2 L"],
    ["Prior thoracic RT", "Distant metastases"],
    ["Definitively showed dose escalation to 74 Gy is harmful", "Factorial design also tested cetuximab"],
    ["Many technical and centre-volume issues", "Heart dose correlated with survival — a hypothesis, not proof"],
    "60 Gy remains standard. The trial highlighted heart dose as a key factor and the importance of RT quality.")

add("CHART",
    ["Inoperable NSCLC, localised", "Good performance status"],
    ["Distant metastases", "Prior RT"],
    ["Survival benefit from accelerated treatment", "Demonstrated tumour repopulation effect"],
    ["Logistically demanding (three fractions daily for 12 days including weekends)", "No chemotherapy"],
    "Showed treatment time matters in NSCLC, but logistics prevented wide adoption. Concurrent chemoRT superseded it.")

add("Lung ART",
    ["Completely resected NSCLC", "Pathological N2", "Adjuvant chemotherapy allowed"],
    ["Incomplete resection", "Prior thoracic RT"],
    ["Modern 3D-conformal technique", "Randomised data on PORT in pN2"],
    ["Underpowered for OS", "More cardiopulmonary deaths with PORT", "Mediastinal relapse halved but no DFS gain"],
    "Routine PORT is not recommended in pN2. Selected patients (extracapsular extension, multiple stations) may still benefit.")

add("CHISEL",
    ["Peripheral stage I NSCLC (T1–T2a N0)", "Medically inoperable or refused surgery", "PET staging"],
    ["Central tumours", "Prior thoracic RT"],
    ["Showed SABR improves local control vs conventional RT", "Shorter treatment"],
    ["Small (n=101)", "Older conventional RT comparator"],
    "Supports SABR as standard for inoperable early NSCLC, though the sample is small.")

add("SABR-COMET",
    ["1–5 metastases, controlled primary", "ECOG PS 0–1", "Life expectancy ≥6 months"],
    ["Brain metastases >3 cm", "Malignant pleural effusion"],
    ["OS benefit in randomised phase 2", "Long-term follow-up"],
    ["Small (n=99), mixed histology", "Treatment-related deaths (~4.5%)", "Imbalance favouring prostate primaries in SABR arm"],
    "Hypothesis-generating rather than definitive. Phase 3 trials (SABR-COMET-3, -10) are needed before widespread use.")

add("Gomez (MDACC) oligomet NSCLC",
    ["Stage IV NSCLC with ≤3 metastases", "No progression after first-line systemic therapy"],
    ["Progressive disease after first-line therapy", "Brain-only unless treated"],
    ["Large PFS and OS benefit", "Stopped early for benefit"],
    ["Small (n=49)", "Early stopping may overestimate effect", "Pre-immunotherapy era"],
    "Strong signal for consolidative local therapy in oligometastatic NSCLC. Its relevance in the immunotherapy era is being tested.")

add("IPASS",
    ["East Asian patients with advanced adenocarcinoma", "Never or light former smokers", "Chemotherapy-naive"],
    ["Prior chemotherapy", "Unstable brain metastases"],
    ["Showed EGFR mutation predicts benefit", "Defined biomarker-driven therapy"],
    ["Clinical rather than molecular selection", "OS not different because of crossover"],
    "Benefit of gefitinib was confined to EGFR-mutant tumours — the trial that made molecular testing mandatory.")

add("FLAURA",
    ["Advanced NSCLC with EGFR exon 19 deletion or L858R", "Treatment-naive", "Stable CNS metastases allowed"],
    ["Prior EGFR TKI", "Interstitial lung disease"],
    ["PFS and OS benefit", "Better CNS efficacy"],
    ["OS benefit not seen in Asian subgroup", "Comparator first-generation TKIs; T790M sequencing not fully used"],
    "Osimertinib became first-line standard. The Asian subgroup result and comparator choice draw criticism.")

add("FLAURA2",
    ["Advanced EGFR-mutant NSCLC", "Treatment-naive", "ECOG PS 0–1"],
    ["Prior EGFR TKI", "Interstitial lung disease"],
    ["PFS and OS benefit", "Benefit greater in CNS metastases and L858R"],
    ["More toxicity from chemotherapy", "Unclear who needs intensification upfront"],
    "Adding chemotherapy to osimertinib improves outcomes, but at a toxicity cost; best suited to higher-risk patients (CNS metastases, L858R, TP53).")

add("MARIPOSA",
    ["Advanced EGFR-mutant NSCLC", "Treatment-naive"],
    ["Prior EGFR TKI", "Interstitial lung disease"],
    ["PFS and OS benefit over osimertinib"],
    ["IV amivantamab with infusion reactions, rash and VTE", "Prophylactic anticoagulation required", "Cost and chair time"],
    "Effective combination, but toxicity and logistics limit its uptake, especially in resource-limited settings.")

add("ALEX",
    ["Advanced ALK-positive NSCLC", "Treatment-naive", "Asymptomatic CNS metastases allowed"],
    ["Prior ALK inhibitor", "Symptomatic CNS metastases"],
    ["Large PFS benefit and CNS protection", "Long-term follow-up"],
    ["Comparator crizotinib — weak CNS penetration", "OS data immature for long"],
    "Alectinib became standard first-line ALK therapy.")

add("CROWN",
    ["Advanced ALK-positive NSCLC", "Treatment-naive"],
    ["Prior ALK inhibitor"],
    ["Unprecedented 5-year PFS (~60%)", "Excellent CNS control"],
    ["Comparator crizotinib", "CNS/cognitive and metabolic side effects (weight gain, lipids)"],
    "Lorlatinib offers the longest PFS but neurocognitive toxicity requires careful monitoring.")

add("KEYNOTE-024",
    ["Advanced NSCLC, PD-L1 TPS ≥50%", "No EGFR/ALK alterations", "Treatment-naive"],
    ["Active autoimmune disease", "Untreated CNS metastases"],
    ["OS benefit despite crossover", "5-year survival ~30%"],
    ["Selected PD-L1-high population", "Chemotherapy comparator without pemetrexed maintenance in all"],
    "Pembrolizumab monotherapy is standard for PD-L1 ≥50%. Many patients still progress early; chemo-IO is an alternative in high-burden disease.")

add("KEYNOTE-189",
    ["Advanced non-squamous NSCLC", "No EGFR/ALK", "Treatment-naive"],
    ["Active autoimmune disease", "Untreated CNS metastases"],
    ["OS benefit across PD-L1 strata", "Long-term follow-up"],
    ["Smaller benefit in PD-L1 <1%", "Toxicity, including nephritis"],
    "Chemo-pembrolizumab is standard for non-squamous NSCLC regardless of PD-L1.")

add("KEYNOTE-407",
    ["Advanced squamous NSCLC", "Treatment-naive"],
    ["Active autoimmune disease", "Untreated CNS metastases"],
    ["OS benefit across PD-L1 levels"],
    ["Smaller benefit in PD-L1 <1%"],
    "Chemo-pembrolizumab is standard for squamous NSCLC.")

add("CheckMate 9LA",
    ["Advanced NSCLC, no EGFR/ALK", "Treatment-naive", "ECOG PS 0–1"],
    ["Active autoimmune disease"],
    ["OS benefit, especially in squamous and PD-L1 <1%", "Short chemotherapy course"],
    ["Higher immune toxicity with ipilimumab", "No direct comparison with chemo-pembrolizumab"],
    "An option for PD-L1-negative or squamous disease; toxicity is a trade-off.")

add("PARAMOUNT",
    ["Advanced non-squamous NSCLC", "No progression after 4 cycles cisplatin-pemetrexed", "ECOG PS 0–1"],
    ["Squamous histology"],
    ["OS benefit for continuation maintenance"],
    ["Pre-immunotherapy era"],
    "Established pemetrexed maintenance, now incorporated into chemo-IO regimens.")

add("Scagliotti cis-pem vs cis-gem",
    ["Advanced NSCLC, chemotherapy-naive", "ECOG PS 0–1"],
    ["Prior chemotherapy"],
    ["Revealed histology as predictive factor (pemetrexed better in non-squamous)", "Large trial"],
    ["Non-inferiority design; histology finding was a subgroup analysis"],
    "Made histology essential for chemotherapy choice in NSCLC.")

add("Temel early palliative care",
    ["Newly diagnosed metastatic NSCLC", "ECOG PS 0–2", "Within 8 weeks of diagnosis"],
    ["Already receiving palliative care"],
    ["Improved quality of life and mood", "Longer survival despite less aggressive end-of-life care"],
    ["Single centre, small (n=151)", "Survival endpoint secondary"],
    "Strong case for early integrated palliative care; generalisability to resource-limited settings needs local models.")

add("CodeBreaK 200",
    ["KRAS G12C-mutant advanced NSCLC", "Progression after platinum and checkpoint inhibitor"],
    ["Active brain metastases", "Prior KRAS G12C inhibitor"],
    ["First randomised phase 3 of KRAS G12C inhibitor"],
    ["Modest PFS gain, no OS benefit", "Crossover and early dropout in docetaxel arm", "FDA concerns about assessment bias"],
    "Sotorasib is modestly better than docetaxel. The modest benefit and bias concerns led to scepticism.")

add("LIBRETTO-431",
    ["RET fusion-positive advanced non-squamous NSCLC", "Treatment-naive"],
    ["Prior systemic therapy"],
    ["Large PFS benefit over chemo-IO", "Strong CNS activity"],
    ["Rare population", "OS immature"],
    "Supports first-line selpercatinib and broad NGS panels at diagnosis.")

add("DESTINY-Lung01/02",
    ["HER2 (ERBB2)-mutant advanced NSCLC", "Prior systemic therapy"],
    ["History of ILD"],
    ["High response rates", "Lower dose (5.4 mg/kg) reduced ILD"],
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

add("Aupérin PCI meta-analysis",
    ["SCLC in complete remission", "Individual patient data from 7 trials"],
    ["Patients without complete response"],
    ["Showed OS benefit (~5% at 3 years)"],
    ["Mostly limited-stage; brain imaging not mandatory", "Pre-MRI era"],
    "PCI benefits patients with complete response, but with MRI surveillance the case for PCI is being re-examined.")

add("ADRIATIC",
    ["Limited-stage SCLC", "No progression after concurrent platinum-etoposide chemoRT", "PCI allowed"],
    ["Prior immunotherapy", "Pneumonitis"],
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
    ["Treatment-naive ES-SCLC", "ECOG PS 0–1", "Asymptomatic brain metastases allowed"],
    ["Prior immunotherapy", "Active autoimmune disease"],
    ["OS benefit", "Allowed cisplatin or carboplatin"],
    ["No PCI in IO arm; modest benefit"],
    "Confirms chemo-IO as first-line standard in ES-SCLC.")

add("CREST (Slotman)",
    ["ES-SCLC with response to chemotherapy", "WHO PS 0–2"],
    ["Brain metastases", "Progressive disease"],
    ["Improved 2-year OS and intrathoracic control"],
    ["Primary 1-year OS not significant", "Pre-immunotherapy era"],
    "Supports thoracic RT in responders with residual thoracic disease.")

add("DeLLphi-304",
    ["SCLC progressing after platinum chemotherapy", "ECOG PS 0–1", "Treated brain metastases allowed"],
    ["Prior DLL3-targeted therapy"],
    ["OS benefit over chemotherapy"],
    ["Cytokine release syndrome and neurotoxicity", "Inpatient monitoring for first doses"],
    "Tarlatamab is a new second-line standard; logistics of CRS monitoring matter.")
