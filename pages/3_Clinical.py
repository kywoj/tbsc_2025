import streamlit as st
from utils import quiz, show_progress

if "score" not in st.session_state:
     st.session_state.score = 0
if "answered" not in st.session_state:
     st.session_state.answered = {}

st.session_state.current_module = "Clinical"

st.header("3. Clinical Development (Phases I-III)")
st.write("""
Once a drug candidate passes preclinical testing and an IND is accepted, 
it can be tested in people. This stage is known as the **clinical trials phase**.

Clinical trials are conducted in three main stages, each larger and more demanding 
than the one before.

### Phases of Clinical Trials
**Phase 1 (Safety and Dosage)**  
     - Conducted with a small number of healthy volunteers (20–100).  
     - Main goal: assess safety, tolerability, and determine the right dosage range.

**Phase 2 (Efficacy and Side Effects)**  
     - Involves several hundred patients who actually have the disease.  
     - Main goal: test whether the drug works as intended and monitor short-term side effects.

**Phase 3 (Confirmation and Comparison)**  
     - Large, often global trials with thousands of patients.  
     - Main goal: confirm effectiveness, collect more safety data, and compare the drug to standard treatments or placebos.

### Key Principles
- **Randomization** – Patients are randomly assigned to different groups 
(drug, placebo, comparator) to reduce bias.
- **Blinding** – In many trials, patients and/or doctors don’t know who is receiving the drug 
to ensure objective results.
- **Endpoints** – Each trial defines measurable outcomes (e.g., reduced symptoms, improved survival).

Clinical trials are long, expensive, and risky. Most drug candidates fail during this stage, but those that succeed provide the strongest  evidence that a drug can truly benefit patients.
""")

module_keys = ["clin1","clin2","clin3","clin4","clin5"]
show_progress(module_keys)

st.subheader("Test your Knowledge")
quiz("Phase 1 trials primarily test…", 
     ["Drug efficacy", "Safety and dosage", "Market demand"], 1, "clin1")
quiz("Phase 2 trials focus on…", 
     ["Long-term side effects", "Proof of concept in patients", "Mass marketing"], 1, "clin2")
quiz("Randomization helps…", 
     ["Reduce bias", "Increase sales", "Accelerate FDA review"], 0, "clin3")
quiz("A placebo is…", 
     ["An inactive substance", "A competitor drug", "A toxic compound"], 0, "clin4")
quiz("Phase 3 trials usually involve…", 
     ["Dozens of patients", "Thousands of patients", "Single healthy volunteers"], 1, "clin5")

st.markdown("---")
