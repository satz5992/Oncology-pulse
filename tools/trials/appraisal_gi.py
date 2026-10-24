# Critical appraisal for GI trials. Revision aid; verify against the primary paper.
A = {}
def add(name, inc, exc, pros, cons, critique):
    A[name] = {"inclusion": inc, "exclusion": exc, "strengths": pros, "limitations": cons, "critique": critique}

# Oesophagus & stomach
add("CROSS",
    ["Resectable oesophageal or GEJ carcinoma (SCC or adenocarcinoma)", "T1N1 or T2–3N0–1, M0", "WHO PS 0–2, weight loss ≤10%"],
    ["Tumour >8 cm or >5 cm wide", "Prior chemotherapy or RT"],
    ["OS benefit with long-term follow-up", "Low-toxicity regimen with high pCR (49% in SCC)"],
    ["Few T4 or bulky tumours", "Larger benefit in SCC than adenocarcinoma"],
    "Standard neoadjuvant chemoRT, especially for SCC. For adenocarcinoma, ESOPEC has challenged it in favour of FLOT.")

add("CheckMate 577",
    ["Stage II–III oesophageal/GEJ cancer", "Residual pathological disease after neoadjuvant chemoRT and R0 resection", "ECOG PS 0–1"],
    ["pCR after surgery", "Prior immunotherapy"],
    ["Doubled DFS in a high-risk group"],
    ["No OS benefit reported", "Mainly adenocarcinoma", "Does not address patients receiving FLOT"],
    "Adjuvant nivolumab is standard after CROSS with residual disease, though the absence of OS benefit tempers enthusiasm.")

add("FLOT4",
    ["Resectable gastric or GEJ adenocarcinoma, ≥cT2 or cN+", "ECOG PS 0–1"],
    ["Distant metastases", "Prior chemotherapy"],
    ["OS benefit over ECF/ECX", "Higher R0 resection"],
    ["Only ~50% completed postoperative chemotherapy", "Toxicity (neutropenia)"],
    "FLOT is the perioperative standard in fit patients; the postoperative phase is hard to complete.")

add("ESOPEC",
    ["Resectable oesophageal adenocarcinoma cT1N+ or cT2–4a any N", "Fit for surgery and both regimens"],
    ["SCC histology", "Distant metastases"],
    ["Head-to-head OS comparison favouring FLOT"],
    ["Open-label; CROSS arm had low adjuvant therapy use", "Not all CROSS patients received nivolumab"],
    "Favours perioperative FLOT for oesophageal adenocarcinoma. Critics note the CROSS arm lacked adjuvant nivolumab now standard.")

add("MAGIC",
    ["Resectable gastric, GEJ or lower oesophageal adenocarcinoma", "Stage II or higher"],
    ["Distant metastases", "Prior chemotherapy"],
    ["First to show OS benefit for perioperative chemotherapy"],
    ["Only ~42% completed all planned treatment", "Limited D2 lymphadenectomy"],
    "Established perioperative chemotherapy, now superseded by FLOT.")

add("INT-0116 (Macdonald)",
    ["Resected gastric or GEJ adenocarcinoma, stage IB–IV (M0)", "Adequate organ function"],
    ["Prior therapy", "Distant metastases"],
    ["OS benefit for adjuvant chemoRT"],
    ["Only ~10% had D2 dissection — chemoRT compensated for inadequate surgery", "Older 5-FU/LV regimen"],
    "Benefit largely reflects inadequate surgery. After D2 gastrectomy, adjuvant chemotherapy (CLASSIC) is preferred; ARTIST trials showed limited added value of RT.")

add("CLASSIC",
    ["Stage II–IIIB gastric cancer", "D2 gastrectomy with R0 resection"],
    ["Prior chemotherapy or RT"],
    ["DFS and OS benefit for adjuvant CAPOX after D2"],
    ["East Asian population", "No comparison with perioperative chemotherapy"],
    "Adjuvant CAPOX is standard after upfront D2 gastrectomy.")

add("ToGA",
    ["HER2-positive (IHC 3+ or FISH+) advanced gastric/GEJ adenocarcinoma", "Treatment-naive"],
    ["Prior anti-HER2 therapy", "Heart failure"],
    ["OS benefit", "Defined HER2 testing in gastric cancer"],
    ["Benefit mainly in IHC 3+ or IHC 2+/FISH+", "Heterogeneous HER2 expression"],
    "Trastuzumab with chemotherapy is standard for HER2+ gastric cancer; proper HER2 scoring is crucial.")

add("KEYNOTE-811",
    ["HER2-positive advanced gastric/GEJ adenocarcinoma", "Treatment-naive"],
    ["Prior immunotherapy", "Active autoimmune disease"],
    ["Higher ORR and PFS/OS benefit"],
    ["Benefit restricted to PD-L1 CPS ≥1", "Initial approval based on ORR"],
    "Adds pembrolizumab for PD-L1-positive HER2+ disease.")

add("CheckMate 649",
    ["HER2-negative advanced gastric, GEJ or oesophageal adenocarcinoma", "Treatment-naive", "ECOG PS 0–1"],
    ["Known HER2-positive", "Active autoimmune disease"],
    ["OS benefit", "Large global trial"],
    ["Benefit concentrated in CPS ≥5", "Little benefit in CPS <1"],
    "Nivolumab plus chemotherapy is standard, ideally for higher PD-L1 expressers.")

add("SPOTLIGHT / GLOW",
    ["Claudin 18.2-positive (≥75% tumour cells moderate-strong), HER2-negative gastric/GEJ adenocarcinoma", "Treatment-naive"],
    ["HER2-positive", "Gastric outlet obstruction"],
    ["OS benefit in a new biomarker-selected population"],
    ["Nausea and vomiting are frequent", "Not compared with nivolumab-chemo"],
    "Zolbetuximab adds a targeted option; sequencing with IO remains unclear.")

add("RAINBOW",
    ["Advanced gastric/GEJ adenocarcinoma", "Progression within 4 months of first-line platinum + fluoropyrimidine"],
    ["Prior paclitaxel", "Uncontrolled hypertension or bleeding"],
    ["OS benefit"],
    ["Modest gain (~2 months)"],
    "Ramucirumab-paclitaxel remains a second-line standard.")

add("CheckMate 648 / KEYNOTE-590",
    ["Advanced or metastatic oesophageal SCC (KN-590 also adenocarcinoma/GEJ)", "Treatment-naive"],
    ["Prior systemic therapy for advanced disease", "Active autoimmune disease"],
    ["OS benefit"],
    ["Benefit driven by PD-L1-positive tumours"],
    "Chemo-IO is first-line standard for oesophageal SCC, particularly with PD-L1 expression.")

add("RTOG 85-01",
    ["Oesophageal cancer T1–3, N0–1, M0", "Suitable for non-surgical treatment"],
    ["Distant metastases", "Tracheo-oesophageal fistula"],
    ["Showed chemoRT superior to RT alone, with long-term survivors"],
    ["Small trial", "Older RT techniques"],
    "Basis for definitive chemoRT in oesophageal cancer.")

add("INT 0123",
    ["Oesophageal cancer T1–4, N0–1, M0", "Definitive chemoRT"],
    ["Distant metastases"],
    ["Showed no benefit for dose escalation"],
    ["Most deaths in high-dose arm occurred before 50.4 Gy", "Older RT technique"],
    "50.4 Gy remains standard. The high-dose arm's excess deaths occurred at low dose, so the trial's conclusion is often debated.")

# Colorectal
add("MOSAIC",
    ["Stage II–III resected colon cancer", "Within 7 weeks of surgery"],
    ["Prior chemotherapy"],
    ["DFS and OS benefit for stage III"],
    ["No OS benefit in stage II", "Oxaliplatin neuropathy"],
    "FOLFOX is standard for stage III; stage II benefit is minimal.")

add("IDEA",
    ["Stage III colon cancer after resection", "Individual data from 6 trials"],
    ["Stage II (separate analysis)"],
    ["Large pooled analysis guiding risk-based duration"],
    ["Non-inferiority overall not met", "Regimen choice not randomised"],
    "3 months CAPOX for low-risk stage III is standard, reducing neuropathy; FOLFOX for 6 months for high-risk disease.")

add("ATOMIC",
    ["Resected stage III dMMR colon cancer", "ECOG PS 0–1"],
    ["Prior therapy"],
    ["Large DFS benefit", "Biomarker-defined population"],
    ["OS data immature", "Small subset of colon cancer"],
    "Adding atezolizumab to FOLFOX is a new standard for stage III dMMR colon cancer.")

add("NICHE-2",
    ["Locally advanced dMMR colon cancer", "Non-metastatic"],
    ["Prior therapy"],
    ["Very high pCR rate (~68%) with short IO"],
    ["Single-arm", "Long-term outcomes awaited"],
    "Strong signal for neoadjuvant IO in dMMR colon cancer; randomised data are needed.")

add("Cercek dostarlimab dMMR rectal",
    ["Stage II–III dMMR rectal cancer", "Treatment-naive"],
    ["Distant metastases"],
    ["100% clinical complete response in early cohort", "Organ preservation without surgery or RT"],
    ["Small single-arm study", "Long-term durability uncertain"],
    "Paradigm-shifting for dMMR rectal cancer; small numbers mean careful follow-up remains essential.")

add("German CAO/ARO/AIO-94",
    ["Stage II–III rectal adenocarcinoma", "Within 16 cm of anal verge"],
    ["Distant metastases", "Prior pelvic RT"],
    ["Lower local recurrence and toxicity with preoperative chemoRT"],
    ["No OS difference"],
    "Preoperative chemoRT became standard.")

add("Dutch TME",
    ["Resectable rectal adenocarcinoma", "No distant metastases"],
    ["Prior pelvic RT"],
    ["Standardised TME surgery with quality control", "Long follow-up"],
    ["No OS benefit overall", "Benefit mainly in middle/low tumours"],
    "Short-course RT reduces local recurrence even with good TME surgery.")

add("RAPIDO",
    ["High-risk locally advanced rectal cancer (cT4, N2, EMVI+, MRF+, lateral nodes)"],
    ["Distant metastases"],
    ["Reduced disease-related treatment failure", "Doubled pCR"],
    ["Higher locoregional recurrence in long-term follow-up", "No OS benefit"],
    "Supports total neoadjuvant therapy, but concerns about local recurrence remain.")

add("PRODIGE 23",
    ["cT3–4 rectal adenocarcinoma", "ECOG PS 0–1"],
    ["Distant metastases"],
    ["DFS and later OS benefit"],
    ["Intensive regimen", "Toxicity"],
    "Total neoadjuvant therapy with FOLFIRINOX improves outcomes for fit patients.")

add("OPRA",
    ["Stage II–III rectal adenocarcinoma"],
    ["Distant metastases"],
    ["Organ preservation in ~half with consolidation chemotherapy"],
    ["Phase 2", "Compared to historical TME outcomes"],
    "Watch-and-wait is feasible with consolidation TNT; long-term data needed.")

add("PROSPECT",
    ["cT2N+ / cT3N0–1 rectal cancer", "Candidates for sphincter-sparing surgery"],
    ["T4", "Low tumours requiring APR"],
    ["Showed FOLFOX alone is non-inferior to chemoRT", "Less long-term toxicity"],
    ["Only intermediate-risk patients", "Requires high-quality MRI"],
    "Pelvic RT can be omitted in selected intermediate-risk rectal cancer.")

add("CRYSTAL",
    ["Metastatic CRC, first line", "EGFR-expressing"],
    ["Prior systemic therapy"],
    ["OS benefit in KRAS wild-type"],
    ["Retrospective biomarker analysis", "Skin toxicity"],
    "Established anti-EGFR in RAS wild-type mCRC.")

add("FIRE-3 / CALGB 80405",
    ["RAS wild-type metastatic CRC", "Treatment-naive"],
    ["Prior systemic therapy"],
    ["Head-to-head comparison", "Showed sidedness matters"],
    ["Primary endpoints not met", "Retrospective sidedness analysis"],
    "Anti-EGFR preferred for left-sided RAS wild-type tumours.")

add("PARADIGM",
    ["RAS wild-type metastatic CRC", "Treatment-naive"],
    ["BRAF mutation", "Prior therapy"],
    ["Prospective confirmation of left-sided benefit"],
    ["Japanese population only"],
    "Panitumumab-FOLFOX is standard for left-sided RAS/BRAF wild-type mCRC.")

add("KEYNOTE-177",
    ["MSI-H/dMMR metastatic CRC", "Treatment-naive"],
    ["Prior systemic therapy"],
    ["Doubled PFS", "Better quality of life"],
    ["Early progression in ~30%", "OS not statistically significant due to crossover"],
    "Pembrolizumab is first-line standard for MSI-H mCRC; early progressors need attention.")

add("CheckMate 8HW",
    ["MSI-H/dMMR metastatic CRC"],
    ["Prior immunotherapy"],
    ["Superior PFS with dual IO"],
    ["More toxicity", "OS immature"],
    "Nivolumab-ipilimumab is an option; toxicity balance needed.")

add("BEACON CRC / BREAKWATER",
    ["BRAF V600E metastatic CRC", "BEACON: after 1–2 lines; BREAKWATER: first line"],
    ["Prior BRAF/EGFR inhibitor"],
    ["OS benefit in a poor-prognosis group"],
    ["Triplet arm not superior in BEACON", "Cost"],
    "Encorafenib-cetuximab is standard; first-line combination with FOLFOX is now emerging.")

add("DESTINY-CRC / MOUNTAINEER",
    ["HER2-positive, RAS wild-type metastatic CRC", "Previously treated"],
    ["Prior anti-HER2 therapy"],
    ["High response rates"],
    ["Single-arm", "ILD risk with T-DXd"],
    "Supports HER2 testing in mCRC; randomised data are limited.")

add("CORRECT / RECOURSE / SUNLIGHT",
    ["Refractory metastatic CRC", "Prior standard therapies"],
    ["Prior regorafenib or FTD-TPI (by trial)"],
    ["OS benefit", "SUNLIGHT showed added benefit with bevacizumab"],
    ["Modest gains", "Toxicity (regorafenib hand-foot syndrome)"],
    "FTD-TPI + bevacizumab is preferred; regorafenib remains an option.")

add("FRESCO-2",
    ["Refractory metastatic CRC after standard therapies"],
    ["Prior fruquintinib"],
    ["OS benefit in heavily pretreated patients"],
    ["Modest benefit"],
    "Fruquintinib is an additional late-line option.")

add("EORTC 40983 (EPOC)",
    ["Resectable colorectal liver metastases (≤4)"],
    ["Extrahepatic disease"],
    ["PFS benefit"],
    ["No OS benefit", "Underpowered"],
    "Perioperative FOLFOX is reasonable; OS benefit unproven.")

# Anal
add("ACT II",
    ["Anal SCC, non-metastatic"],
    ["Prior pelvic RT"],
    ["Large trial", "Showed maintenance chemo not needed"],
    ["Few HIV-positive patients"],
    "5-FU/mitomycin with RT remains standard.")

add("RTOG 98-11",
    ["Anal SCC T2–4, any N"],
    ["Distant metastases"],
    ["Showed cisplatin induction inferior"],
    ["Induction delayed RT"],
    "Confirmed mitomycin-based chemoRT as standard.")

add("POD1UM-303",
    ["Advanced anal SCC", "Treatment-naive"],
    ["Prior immunotherapy"],
    ["PFS benefit"],
    ["OS immature"],
    "First positive IO trial in anal cancer; adds retifanlimab to first-line chemotherapy.")

# Pancreas
add("CONKO-001",
    ["Resected pancreatic adenocarcinoma (R0/R1)"],
    ["Prior therapy", "CA19-9 >2.5× ULN post-op"],
    ["DFS and OS benefit"],
    ["Small absolute benefit"],
    "Established adjuvant gemcitabine.")

add("ESPAC-4",
    ["Resected pancreatic adenocarcinoma"],
    ["Prior therapy"],
    ["OS benefit with gemcitabine-capecitabine"],
    ["Small gain"],
    "Gem-cap is an option for patients unfit for FOLFIRINOX.")

add("PRODIGE 24",
    ["Resected pancreatic adenocarcinoma, PS 0–1", "CA19-9 <180 U/mL"],
    ["Prior therapy"],
    ["Large OS benefit"],
    ["Fit patients only", "Toxicity"],
    "mFOLFIRINOX is the adjuvant standard for fit patients.")

add("ACCORD 11 (PRODIGE 4)",
    ["Metastatic pancreatic cancer, ECOG PS 0–1", "Age ≤75", "Bilirubin ≤1.5× ULN"],
    ["Prior chemotherapy"],
    ["OS benefit"],
    ["Toxicity", "Fit patients only"],
    "FOLFIRINOX is standard for fit patients.")

add("MPACT",
    ["Metastatic pancreatic cancer, KPS ≥70"],
    ["Prior therapy"],
    ["OS benefit"],
    ["Neuropathy"],
    "Gem-nab-paclitaxel is standard for less-fit patients.")

add("NAPOLI-3",
    ["Metastatic pancreatic cancer, ECOG PS 0–1", "Treatment-naive"],
    ["Prior therapy"],
    ["OS benefit over gem-nab-paclitaxel"],
    ["Modest gain", "Comparison with FOLFIRINOX absent"],
    "NALIRIFOX is an option; cost-effectiveness vs FOLFIRINOX is debated.")

add("POLO",
    ["gBRCA metastatic pancreatic cancer", "No progression after ≥16 weeks platinum"],
    ["Prior PARP inhibitor"],
    ["PFS benefit"],
    ["No OS benefit"],
    "Olaparib maintenance is an option; continuing platinum is a reasonable alternative.")

add("RASolute 302",
    ["Previously treated metastatic pancreatic adenocarcinoma", "RAS-mutant or wild-type"],
    ["Prior RAS inhibitor"],
    ["OS benefit"],
    ["Data recently published; long-term data limited"],
    "Daraxonrasib offers a new option; confirmation of benefit in all subgroups needed.")

add("PREOPANC",
    ["Resectable or borderline resectable pancreatic cancer"],
    ["Distant metastases"],
    ["Long-term OS benefit"],
    ["Gemcitabine-based regimen, not modern multi-agent"],
    "Neoadjuvant therapy supported; optimal regimen remains under study.")

# Hepatobiliary
add("SHARP",
    ["Advanced HCC, Child-Pugh A", "ECOG PS 0–2"],
    ["Prior systemic therapy"],
    ["First systemic therapy to improve OS"],
    ["Modest benefit"],
    "Established systemic therapy for HCC, now superseded.")

add("REFLECT",
    ["Unresectable HCC, Child-Pugh A"],
    ["≥50% liver involvement", "Main portal vein invasion"],
    ["Non-inferior OS"],
    ["Excluded high-risk patients"],
    "Lenvatinib is an alternative first-line option.")

add("IMbrave150",
    ["Unresectable HCC, Child-Pugh A", "Treatment-naive"],
    ["Untreated varices", "Autoimmune disease"],
    ["OS benefit"],
    ["Bleeding risk"],
    "Atezolizumab-bevacizumab is first-line standard; endoscopy for varices required.")

add("HIMALAYA",
    ["Unresectable HCC, Child-Pugh A"],
    ["Main portal vein thrombosis"],
    ["Durable OS benefit", "No bleeding risk"],
    ["Immune toxicity"],
    "STRIDE is an option for patients with bleeding risk.")

add("CheckMate 9DW",
    ["Unresectable HCC, Child-Pugh A"],
    ["Prior systemic therapy"],
    ["OS benefit"],
    ["Immune toxicity"],
    "Nivo-ipi is another first-line option.")

add("TOPAZ-1",
    ["Advanced biliary tract cancer", "Treatment-naive"],
    ["Prior systemic therapy"],
    ["OS benefit"],
    ["Modest gain"],
    "Durvalumab-gem-cis is first-line standard.")

add("ABC-02",
    ["Advanced biliary tract cancer"],
    ["Prior chemotherapy"],
    ["OS benefit"],
    ["Pre-IO era"],
    "Established gem-cis as standard.")

add("BILCAP",
    ["Resected biliary tract cancer"],
    ["Prior therapy"],
    ["OS benefit in per-protocol analysis"],
    ["ITT not significant"],
    "Capecitabine is standard adjuvant therapy, though the evidence is modest.")

add("ClarIDHy / FIGHT-202",
    ["IDH1-mutant (ClarIDHy) or FGFR2-fusion (FIGHT-202) cholangiocarcinoma", "Previously treated"],
    ["Prior targeted therapy"],
    ["Established targeted therapy in biliary cancer"],
    ["FIGHT-202 single-arm", "Modest PFS in ClarIDHy"],
    "Supports molecular testing in cholangiocarcinoma.")

# NET
add("NETTER-1",
    ["SSTR-positive midgut NET", "Progressing on octreotide"],
    ["Prior PRRT"],
    ["Large PFS benefit"],
    ["Open-label", "OS difference not significant"],
    "PRRT is standard second-line therapy for midgut NET.")

add("NETTER-2",
    ["Newly diagnosed SSTR+ G2/G3 GEP-NET (Ki-67 10–55%)"],
    ["Prior PRRT"],
    ["PFS benefit in first line"],
    ["OS immature"],
    "First-line PRRT is an option for higher-grade NETs.")

add("PROMID / CLARINET",
    ["Well-differentiated GEP-NET"],
    ["Prior SSA"],
    ["PFS benefit"],
    ["No OS benefit"],
    "SSAs are first-line therapy for NETs.")

add("RADIANT-3/4 & SUN-1111",
    ["Advanced pancreatic (RADIANT-3, SUN) or lung/GI NET (RADIANT-4)"],
    ["Prior mTOR or VEGF therapy"],
    ["PFS benefit"],
    ["No OS benefit"],
    "Everolimus and sunitinib are options after SSAs.")

add("E2211 (CAPTEM)",
    ["Advanced pancreatic NET"],
    ["Prior temozolomide"],
    ["PFS and OS benefit"],
    ["Myelosuppression"],
    "CAPTEM is an effective option for pancreatic NETs.")
