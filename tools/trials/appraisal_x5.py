# Depth pass: lung leftovers, oesophagus/stomach, colorectal.
A = {}
def add(name, inc, exc, pros, cons, critique):
    A[name] = {"inclusion": inc, "exclusion": exc, "strengths": pros, "limitations": cons, "critique": critique}

add("MARIPOSA",
    ["Advanced EGFR-mutant (ex19del/L858R) NSCLC", "Treatment-naive", "ECOG PS 0–1"],
    ["Prior EGFR TKI", "History of ILD", "Untreated or symptomatic brain metastases"],
    ["PFS and OS benefit over osimertinib", "Benefit in high-risk subgroups (TP53, liver metastases)"],
    ["IV amivantamab with infusion reactions, rash, paronychia and VTE", "Prophylactic anticoagulation needed", "Cost and chair time"],
    "Effective combination, but toxicity and logistics limit uptake, especially in resource-limited settings. A subcutaneous formulation may help.")

add("CheckMate 9LA",
    ["Advanced NSCLC (squamous or non-squamous)", "No EGFR/ALK alterations", "Treatment-naive, ECOG PS 0–1"],
    ["Active autoimmune disease", "Untreated CNS metastases", "Prior systemic therapy for advanced disease"],
    ["OS benefit, especially in squamous and PD-L1 <1%", "Only 2 cycles of chemotherapy limit cumulative toxicity"],
    ["Higher immune toxicity from ipilimumab", "No direct comparison with chemo-pembrolizumab"],
    "An option for PD-L1-negative or squamous disease where dual checkpoint blockade may add durability; toxicity is the trade-off.")

add("Scagliotti cis-pem vs cis-gem",
    ["Advanced (IIIB/IV) NSCLC, chemotherapy-naive", "ECOG PS 0–1"],
    ["Prior chemotherapy", "Symptomatic brain metastases", "Inability to take folic acid/B12"],
    ["Revealed histology as a predictive factor", "Large trial (n=1,725)"],
    ["Non-inferiority design; histology finding was a pre-planned subgroup", "Pre-molecular era"],
    "Made histology essential for chemotherapy choice — pemetrexed for non-squamous, gemcitabine for squamous.")

add("LIBRETTO-431",
    ["RET fusion-positive advanced non-squamous NSCLC", "Treatment-naive", "ECOG PS 0–2"],
    ["Prior systemic therapy for advanced disease", "Symptomatic CNS metastases"],
    ["Large PFS benefit over chemo-pembrolizumab", "Strong CNS activity"],
    ["Rare population (~1–2% of NSCLC)", "OS immature", "Open-label"],
    "Supports first-line selpercatinib and broad NGS panels at diagnosis.")

add("DESTINY-Lung01/02",
    ["HER2 (ERBB2)-mutant advanced NSCLC", "Prior systemic therapy", "ECOG PS 0–1"],
    ["History of ILD requiring steroids", "Untreated brain metastases"],
    ["High response rates (~50%)", "Lower dose (5.4 mg/kg) reduced ILD"],
    ["Non-randomised", "ILD risk"],
    "Led to accelerated approval; randomised data are pending. ILD monitoring is essential.")

add("ADRIATIC",
    ["Limited-stage SCLC", "No progression after concurrent platinum-etoposide chemoRT", "PCI allowed"],
    ["Prior immunotherapy", "Grade ≥2 pneumonitis", "Active autoimmune disease"],
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
    ["Improved 2-year OS and intrathoracic control", "Low-toxicity regimen"],
    ["Primary 1-year OS endpoint not met", "Pre-immunotherapy era", "30 Gy/10 fractions — low dose"],
    "Supports consolidative thoracic RT in responders with residual thoracic disease; its role with IO is under study.")

add("DeLLphi-304",
    ["SCLC progressing after first-line platinum chemotherapy (± immunotherapy)", "ECOG PS 0–1", "Treated, stable brain metastases allowed"],
    ["Prior DLL3-targeted therapy", "Symptomatic CNS metastases"],
    ["OS benefit over standard chemotherapy", "Better tolerability than chemotherapy"],
    ["Cytokine release syndrome and neurotoxicity", "Requires inpatient monitoring for first doses"],
    "Tarlatamab is a new second-line standard; logistics of CRS monitoring matter.")

add("CheckMate 577",
    ["Stage II–III oesophageal/GEJ cancer", "Residual pathological disease after neoadjuvant chemoRT and R0 resection", "ECOG PS 0–1"],
    ["pCR after surgery", "Prior immunotherapy", "Active autoimmune disease"],
    ["Doubled DFS in a high-risk group", "Double-blind, placebo-controlled"],
    ["No OS benefit reported", "Mainly adenocarcinoma", "Does not address patients receiving FLOT"],
    "Adjuvant nivolumab is standard after CROSS with residual disease, though the absence of OS benefit tempers enthusiasm.")

add("ESOPEC",
    ["Resectable oesophageal adenocarcinoma cT1N+ or cT2–4a any N", "Fit for surgery and both regimens"],
    ["SCC histology", "Distant metastases"],
    ["Head-to-head OS comparison favouring FLOT", "Multicentre German trial"],
    ["Open-label; CROSS arm had low adjuvant therapy use", "Not all CROSS patients received nivolumab"],
    "Favours perioperative FLOT for oesophageal adenocarcinoma. Critics note the CROSS arm lacked adjuvant nivolumab now standard.")

add("MAGIC",
    ["Resectable gastric, GEJ or lower oesophageal adenocarcinoma", "Stage II or higher", "WHO PS 0–1"],
    ["Distant metastases", "Prior chemotherapy"],
    ["First to show OS benefit for perioperative chemotherapy (5-year OS 36% vs 23%)", "Multicentre UK trial"],
    ["Only ~42% completed all planned treatment", "Limited D2 lymphadenectomy", "ECF is now outdated"],
    "Established perioperative chemotherapy; FLOT has since superseded ECF.")

add("INT-0116 (Macdonald)",
    ["Resected gastric or GEJ adenocarcinoma, stage IB–IV (M0)", "Adequate organ function"],
    ["Prior therapy", "Distant metastases"],
    ["OS benefit for adjuvant chemoRT", "Long-term follow-up"],
    ["Only ~10% had D2 dissection — chemoRT compensated for inadequate surgery", "Older 5-FU/LV regimen"],
    "Benefit largely reflects inadequate surgery. After D2 gastrectomy, adjuvant chemotherapy (CLASSIC) is preferred; ARTIST trials showed limited added value of RT.")

add("KEYNOTE-811",
    ["HER2-positive advanced gastric/GEJ adenocarcinoma", "Treatment-naive", "ECOG PS 0–1"],
    ["Prior immunotherapy", "Active autoimmune disease", "Untreated CNS metastases"],
    ["Higher ORR and PFS/OS benefit", "Double-blind"],
    ["Benefit restricted to PD-L1 CPS ≥1", "Initial approval based on ORR alone"],
    "Adds pembrolizumab for PD-L1-positive HER2+ disease.")

add("CheckMate 649",
    ["HER2-negative advanced gastric, GEJ or oesophageal adenocarcinoma", "Treatment-naive", "ECOG PS 0–1"],
    ["Known HER2-positive", "Active autoimmune disease", "Untreated CNS metastases"],
    ["OS benefit", "Large global trial including Asian patients"],
    ["Benefit concentrated in CPS ≥5", "Little or no benefit in CPS <1"],
    "Nivolumab plus chemotherapy is standard, ideally for higher PD-L1 expressers.")

add("SPOTLIGHT / GLOW",
    ["Claudin 18.2-positive (≥75% tumour cells moderate-strong staining), HER2-negative gastric/GEJ adenocarcinoma", "Treatment-naive"],
    ["HER2-positive", "Gastric outlet obstruction or complete dysphagia", "Prior systemic therapy"],
    ["OS benefit in a new biomarker-selected population", "Two concordant phase 3 trials"],
    ["Nausea and vomiting are frequent, especially with first dose", "Not compared with nivolumab-chemo"],
    "Zolbetuximab adds a targeted option; sequencing with IO remains unclear.")

add("RAINBOW",
    ["Advanced gastric/GEJ adenocarcinoma", "Progression within 4 months of first-line platinum + fluoropyrimidine", "ECOG PS 0–1"],
    ["Prior paclitaxel", "Uncontrolled hypertension or major bleeding"],
    ["OS benefit (9.6 vs 7.4 months)", "Double-blind"],
    ["Modest gain", "Neutropenia and hypertension"],
    "Ramucirumab-paclitaxel remains a second-line standard.")

add("CheckMate 648 / KEYNOTE-590",
    ["Advanced or metastatic oesophageal SCC (KN-590 also adenocarcinoma/Siewert I GEJ)", "Treatment-naive", "ECOG PS 0–1"],
    ["Prior systemic therapy for advanced disease", "Active autoimmune disease"],
    ["OS benefit", "Large global trials with Asian representation"],
    ["Benefit driven by PD-L1-positive tumours (CPS ≥10 / TPS ≥1%)", "Little benefit in PD-L1-negative tumours"],
    "Chemo-IO is first-line standard for oesophageal SCC, particularly with PD-L1 expression.")

add("RTOG 85-01",
    ["Oesophageal cancer T1–3, N0–1, M0", "Suitable for non-surgical treatment"],
    ["Distant metastases", "Tracheo-oesophageal fistula"],
    ["Showed chemoRT superior to RT alone", "Long-term survivors (~26% at 5 years)"],
    ["Small trial", "Older RT techniques"],
    "Basis for definitive chemoRT in oesophageal cancer.")

add("INT 0123",
    ["Oesophageal cancer T1–4, N0–1, M0", "Selected for definitive chemoRT"],
    ["Distant metastases", "Tracheo-oesophageal fistula"],
    ["Showed no benefit for dose escalation", "Randomised phase 3"],
    ["Most deaths in high-dose arm occurred before 50.4 Gy", "Older RT technique"],
    "50.4 Gy remains standard. The high-dose arm's excess deaths occurred at low dose, so the trial's conclusion is often debated.")

add("MOSAIC",
    ["Stage II–III resected colon cancer", "Within 7 weeks of surgery", "ECOG PS 0–1"],
    ["Prior chemotherapy", "Peripheral neuropathy"],
    ["DFS and OS benefit for stage III", "Long-term follow-up"],
    ["No OS benefit in stage II", "Oxaliplatin neuropathy can persist"],
    "FOLFOX is standard for stage III; stage II benefit is minimal and limited to high-risk features.")

add("IDEA",
    ["Stage III colon cancer after resection", "Individual data from 6 trials (~12,800 patients)"],
    ["Stage II (separate analysis)", "Metastatic disease"],
    ["Large pooled analysis guiding risk-based duration", "Showed less neuropathy with 3 months"],
    ["Non-inferiority overall not met", "Regimen choice (FOLFOX vs CAPOX) not randomised"],
    "3 months CAPOX for low-risk stage III is standard, reducing neuropathy; 6 months for high-risk disease.")

add("ATOMIC",
    ["Resected stage III dMMR colon cancer", "ECOG PS 0–1"],
    ["Prior systemic therapy", "Active autoimmune disease"],
    ["Large DFS benefit", "Biomarker-defined population"],
    ["OS data immature", "Small subset of colon cancer"],
    "Adding atezolizumab to FOLFOX is a new standard for stage III dMMR colon cancer.")

add("NICHE-2",
    ["Locally advanced (cT3 and/or N+) dMMR colon cancer", "Non-metastatic"],
    ["Prior systemic therapy", "Distant metastases"],
    ["Very high pCR rate (~68%) with short IO", "No delay in surgery"],
    ["Single-arm", "Long-term outcomes awaited"],
    "Strong signal for neoadjuvant IO in dMMR colon cancer; randomised data are needed.")

add("Cercek dostarlimab dMMR rectal",
    ["Stage II–III dMMR rectal adenocarcinoma", "Treatment-naive"],
    ["Distant metastases", "Prior systemic therapy"],
    ["100% clinical complete response in early cohort", "Organ preservation without surgery or RT"],
    ["Small single-arm study", "Long-term durability uncertain"],
    "Paradigm-shifting for dMMR rectal cancer; small numbers mean careful follow-up remains essential.")

add("German CAO/ARO/AIO-94",
    ["Stage II–III rectal adenocarcinoma", "Within 16 cm of anal verge", "Age ≤75"],
    ["Distant metastases", "Prior pelvic RT"],
    ["Lower local recurrence and toxicity with preoperative chemoRT", "Long-term follow-up"],
    ["No OS difference", "Overstaging risk in preoperative arm"],
    "Preoperative chemoRT became standard.")

add("Dutch TME",
    ["Resectable rectal adenocarcinoma", "Within 15 cm of anal verge"],
    ["Prior pelvic RT", "Distant metastases"],
    ["Standardised TME surgery with quality control", "Long follow-up (12 years)"],
    ["No OS benefit overall", "Benefit mainly in middle/low tumours"],
    "Short-course RT reduces local recurrence even with good TME surgery.")

add("RAPIDO",
    ["High-risk locally advanced rectal cancer (cT4, N2, EMVI+, MRF+, lateral nodes)", "ECOG PS 0–1"],
    ["Distant metastases", "Prior pelvic RT"],
    ["Reduced disease-related treatment failure", "Doubled pCR (28% vs 14%)"],
    ["Higher locoregional recurrence in long-term follow-up", "No OS benefit"],
    "Supports total neoadjuvant therapy, but concerns about local recurrence remain.")

add("PRODIGE 23",
    ["cT3–4 rectal adenocarcinoma", "ECOG PS 0–1", "Age 18–75"],
    ["Distant metastases", "Prior pelvic RT"],
    ["DFS and later OS benefit", "Higher pCR"],
    ["Intensive regimen", "Toxicity (neutropenia, diarrhoea)"],
    "Total neoadjuvant therapy with FOLFIRINOX improves outcomes for fit patients.")
