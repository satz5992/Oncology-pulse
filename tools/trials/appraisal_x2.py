# Full-depth rewrites: oesophagus/stomach, colorectal, anal.
A = {}
def add(name, inc, exc, pros, cons, critique):
    A[name] = {"inclusion": inc, "exclusion": exc, "strengths": pros, "limitations": cons, "critique": critique}

add("FLOT4",
    ["Resectable gastric or GEJ adenocarcinoma, cT2+ and/or cN+", "No distant metastases", "ECOG PS 0–1"],
    ["Prior chemotherapy or RT", "Distant metastases", "Significant cardiac disease"],
    ["OS benefit over ECF/ECX (median 50 vs 35 months)", "Higher R0 and pCR rates"],
    ["Only ~50% completed all postoperative cycles", "Neutropenia and neuropathy", "Mostly European population with GEJ predominance"],
    "FLOT is the perioperative standard for fit patients. Many cannot complete the postoperative phase; adding immunotherapy (MATTERHORN) is the next step.")

add("MAGIC",
    ["Resectable gastric, GEJ or lower oesophageal adenocarcinoma", "Stage II or higher", "WHO PS 0–1"],
    ["Distant metastases", "Prior chemotherapy"],
    ["First to show OS benefit for perioperative chemotherapy (5-year OS 36% vs 23%)"],
    ["Only ~42% completed all planned treatment", "Limited D2 lymphadenectomy", "ECF is now outdated"],
    "Established perioperative chemotherapy; FLOT has since superseded ECF.")

add("CLASSIC",
    ["Stage II–IIIB gastric adenocarcinoma", "D2 gastrectomy with R0 resection", "Korean, Chinese and Taiwanese patients"],
    ["Prior chemotherapy or RT", "Distant metastases"],
    ["DFS and OS benefit for adjuvant CAPOX after D2 surgery", "5-year follow-up"],
    ["East Asian population", "No comparison with perioperative chemotherapy"],
    "Adjuvant CAPOX is standard after upfront D2 gastrectomy, which is common practice in India for operable gastric cancer.")

add("ToGA",
    ["HER2-positive (IHC 3+ or FISH+) advanced gastric/GEJ adenocarcinoma", "Treatment-naive for advanced disease", "ECOG PS 0–2"],
    ["Prior anti-HER2 therapy", "Congestive heart failure or LVEF <50%"],
    ["OS benefit (13.8 vs 11.1 months)", "Defined HER2 testing criteria in gastric cancer"],
    ["Benefit mainly in IHC 3+ or IHC 2+/FISH+", "Heterogeneous HER2 expression in gastric tumours"],
    "Trastuzumab with chemotherapy is standard for HER2+ gastric cancer; correct HER2 scoring (gastric-specific criteria) is critical.")

add("KEYNOTE-811",
    ["HER2-positive advanced gastric/GEJ adenocarcinoma", "Treatment-naive", "ECOG PS 0–1"],
    ["Prior immunotherapy", "Active autoimmune disease", "Untreated CNS metastases"],
    ["Higher ORR and PFS/OS benefit"],
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
    ["OS benefit (9.6 vs 7.4 months)"],
    ["Modest gain", "Neutropenia and hypertension"],
    "Ramucirumab-paclitaxel remains a second-line standard.")

add("CheckMate 648 / KEYNOTE-590",
    ["Advanced or metastatic oesophageal SCC (KN-590 also adenocarcinoma/Siewert I GEJ)", "Treatment-naive", "ECOG PS 0–1"],
    ["Prior systemic therapy for advanced disease", "Active autoimmune disease"],
    ["OS benefit", "Large global trials"],
    ["Benefit driven by PD-L1-positive tumours (CPS ≥10 / TPS ≥1%)"],
    "Chemo-IO is first-line standard for oesophageal SCC, particularly with PD-L1 expression.")

add("RTOG 85-01",
    ["Oesophageal cancer T1–3, N0–1, M0", "Suitable for non-surgical treatment"],
    ["Distant metastases", "Tracheo-oesophageal fistula"],
    ["Showed chemoRT superior to RT alone, with long-term survivors (~26% at 5 years)"],
    ["Small trial", "Older RT techniques"],
    "Basis for definitive chemoRT in oesophageal cancer.")

add("INT 0123",
    ["Oesophageal cancer T1–4, N0–1, M0", "Selected for definitive chemoRT"],
    ["Distant metastases", "Tracheo-oesophageal fistula"],
    ["Showed no benefit for dose escalation"],
    ["Most deaths in high-dose arm occurred before 50.4 Gy", "Older RT technique"],
    "50.4 Gy remains standard. The high-dose arm's excess deaths occurred at low dose, so the trial's conclusion is often debated.")

add("MOSAIC",
    ["Stage II–III resected colon cancer", "Within 7 weeks of surgery", "ECOG PS 0–1"],
    ["Prior chemotherapy", "Peripheral neuropathy"],
    ["DFS and OS benefit for stage III", "Long-term follow-up"],
    ["No OS benefit in stage II", "Oxaliplatin neuropathy can persist"],
    "FOLFOX is standard for stage III; stage II benefit is minimal and limited to high-risk features.")

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
    ["Lower local recurrence and toxicity with preoperative chemoRT"],
    ["No OS difference"],
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
    ["DFS and later OS benefit"],
    ["Intensive regimen", "Toxicity (neutropenia, diarrhoea)"],
    "Total neoadjuvant therapy with FOLFIRINOX improves outcomes for fit patients.")

add("OPRA",
    ["Stage II–III rectal adenocarcinoma", "Candidates for TME surgery"],
    ["Distant metastases", "Prior pelvic RT"],
    ["Organ preservation in ~half with consolidation chemotherapy"],
    ["Phase 2", "Compared to historical TME outcomes"],
    "Watch-and-wait is feasible with consolidation TNT; long-term data needed.")

add("PROSPECT",
    ["cT2N+ / cT3N0–1 rectal cancer", "Candidates for sphincter-sparing surgery"],
    ["T4", "Low tumours requiring APR", "Distant metastases"],
    ["Showed FOLFOX alone is non-inferior to chemoRT", "Less long-term toxicity"],
    ["Only intermediate-risk patients", "Requires high-quality MRI staging"],
    "Pelvic RT can be omitted in selected intermediate-risk rectal cancer.")

add("CRYSTAL",
    ["Metastatic CRC, first line", "EGFR-expressing", "ECOG PS 0–2"],
    ["Prior systemic therapy for metastatic disease", "Prior anti-EGFR therapy"],
    ["OS benefit in KRAS wild-type"],
    ["Retrospective biomarker analysis", "Skin toxicity"],
    "Established anti-EGFR therapy in RAS wild-type mCRC.")

add("FIRE-3 / CALGB 80405",
    ["RAS wild-type metastatic CRC", "Treatment-naive"],
    ["Prior systemic therapy for metastatic disease"],
    ["Head-to-head comparison", "Showed sidedness matters"],
    ["Primary endpoints not met", "Retrospective sidedness analysis"],
    "Anti-EGFR preferred for left-sided RAS wild-type tumours.")

add("PARADIGM",
    ["RAS wild-type metastatic CRC", "Treatment-naive", "ECOG PS 0–1"],
    ["BRAF mutation", "Prior systemic therapy"],
    ["Prospective confirmation of left-sided benefit"],
    ["Japanese population only"],
    "Panitumumab-FOLFOX is standard for left-sided RAS/BRAF wild-type mCRC.")

add("KEYNOTE-177",
    ["MSI-H/dMMR metastatic CRC", "Treatment-naive", "ECOG PS 0–1"],
    ["Prior systemic therapy for metastatic disease", "Active autoimmune disease"],
    ["Doubled PFS", "Better quality of life"],
    ["Early progression in ~30%", "OS not statistically significant due to crossover"],
    "Pembrolizumab is first-line standard for MSI-H mCRC; early progressors need attention.")

add("CheckMate 8HW",
    ["MSI-H/dMMR metastatic CRC", "ECOG PS 0–1"],
    ["Prior immunotherapy", "Active autoimmune disease"],
    ["Superior PFS with dual IO"],
    ["More toxicity", "OS immature"],
    "Nivolumab-ipilimumab is an option; toxicity balance needed.")

add("BEACON CRC / BREAKWATER",
    ["BRAF V600E metastatic CRC", "BEACON: after 1–2 lines; BREAKWATER: first line"],
    ["Prior BRAF/EGFR inhibitor", "Active brain metastases"],
    ["OS benefit in a poor-prognosis group"],
    ["Triplet arm not superior in BEACON", "Cost"],
    "Encorafenib-cetuximab is standard; first-line combination with FOLFOX is now emerging.")

add("DESTINY-CRC / MOUNTAINEER",
    ["HER2-positive, RAS wild-type metastatic CRC", "Previously treated"],
    ["Prior anti-HER2 therapy", "History of ILD (DESTINY-CRC)"],
    ["High response rates"],
    ["Single-arm", "ILD risk with T-DXd"],
    "Supports HER2 testing in mCRC; randomised data are limited.")

add("CORRECT / RECOURSE / SUNLIGHT",
    ["Refractory metastatic CRC", "Prior fluoropyrimidine, oxaliplatin, irinotecan, anti-VEGF ± anti-EGFR"],
    ["Prior regorafenib or FTD-TPI (by trial)", "ECOG PS ≥2"],
    ["OS benefit", "SUNLIGHT showed added benefit with bevacizumab"],
    ["Modest gains", "Toxicity (regorafenib hand-foot syndrome)"],
    "FTD-TPI + bevacizumab is preferred; regorafenib remains an option.")

add("FRESCO-2",
    ["Refractory metastatic CRC after standard therapies including FTD-TPI or regorafenib"],
    ["Prior fruquintinib", "Uncontrolled hypertension"],
    ["OS benefit in heavily pretreated patients"],
    ["Modest benefit (~2.6 months)"],
    "Fruquintinib is an additional late-line option.")

add("EORTC 40983 (EPOC)",
    ["Resectable colorectal liver metastases (≤4)", "No extrahepatic disease"],
    ["Prior oxaliplatin", "Extrahepatic disease"],
    ["PFS benefit"],
    ["No OS benefit", "Underpowered"],
    "Perioperative FOLFOX is reasonable; OS benefit unproven.")

add("ACT II",
    ["Anal SCC, non-metastatic", "Age ≥18"],
    ["Prior pelvic RT", "Distant metastases"],
    ["Large trial", "Showed maintenance chemo not needed"],
    ["Few HIV-positive patients"],
    "5-FU/mitomycin with RT remains standard.")

add("RTOG 98-11",
    ["Anal SCC T2–4, any N", "Non-metastatic"],
    ["Distant metastases", "Prior pelvic RT"],
    ["Showed cisplatin induction inferior"],
    ["Induction delayed RT"],
    "Confirmed mitomycin-based chemoRT as standard.")

add("POD1UM-303",
    ["Advanced anal SCC", "Treatment-naive", "ECOG PS 0–1"],
    ["Prior immunotherapy", "Active autoimmune disease"],
    ["PFS benefit"],
    ["OS immature"],
    "First positive IO trial in anal cancer; adds retifanlimab to first-line chemotherapy.")
