import streamlit as st
from utils import quiz, show_progress

if "score" not in st.session_state:
     st.session_state.score = 0
if "answered" not in st.session_state:
     st.session_state.answered = {}

st.session_state.current_module = "Discovery"

st.header("1. Drug Discovery")
st.write("""
The discovery phase is where the journey of a new medicine begins. 
Scientists first need to understand the biology of the disease. 
They ask: *What molecule in the body is going wrong, and how could changing it help patients?*

### Key Steps in Discovery
1. **Target Identification** – Scientists identify a molecule, such as a protein or receptor, 
that plays a critical role in the disease.
2. **Target Validation** – They confirm that influencing this target could realistically 
have a therapeutic effect.
3. **Hit Identification** – Using techniques like high-throughput screening, 
researchers test huge libraries of chemical or biological compounds to see if any bind to the target. 
These initial “hits” show some desired activity.
4. **Hit-to-Lead Optimization** – Promising hits are studied further and modified to 
improve their strength, selectivity, and safety profile.
5. **Lead Optimization & Candidate Selection** – After rounds of refinement, 
the best “lead” compound is chosen as a **preclinical candidate** — 
the one most likely to succeed in lab and animal studies.

Drug discovery is a creative and experimental process. Only a small fraction of initial hits advance to preclinical testing, but this phase lays the foundation for all later steps in developing safe and effective medicines.
""")

module_keys = ["disc1","disc2","disc3","disc4","disc5"]
show_progress(module_keys)

st.subheader("Test your Knowledge")
quiz("What is typically the first step in discovery?", 
     ["Manufacturing scale-up", "Identifying a drug target", "Conducting Phase 1 trials"], 1, "disc1")

quiz("High-throughput screening is used to…", 
     ["Test thousands of compounds quickly", "Regulate FDA approvals", "Analyze patient records"], 0, "disc2")

quiz("A 'hit' compound is…", 
     ["The final approved drug", "A molecule with initial desirable activity", "A placebo"], 1, "disc3")

quiz("Hit-to-lead and lead optimization focus on…", 
     ["Improving drug properties", "Recruiting trial patients", "Filing patents"], 0, "disc4")

quiz("Preclinical candidate selection determines…", 
     ["The final approved drug", "Which compound is most promising to move forward into preclinical testing", "Marketing strategy"], 1, "disc5")

st.markdown("---")
