import streamlit as st
from utils import quiz, show_progress

if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = {}

st.session_state.current_module = "Regulatory"

st.header("4. Regulatory & Commercialization")
st.write("""
Even after years of discovery, preclinical research, and clinical trials, 
a drug cannot be sold until it is formally reviewed by regulatory authorities 
such as the U.S. **Food and Drug Administration (FDA)** or the **European Medicines Agency (EMA)**.

### Submitting for Approval
- All trial data and preclinical results are compiled into a massive document called a 
**New Drug Application (NDA)** or a **Biologics License Application (BLA)**.
- This includes manufacturing processes, labeling, proposed dosing, 
and evidence of safety and effectiveness.

### Regulatory Review
- Regulators carefully evaluate the data to ensure the benefits outweigh the risks.  
- Advisory committees of outside experts may review and recommend approval or rejection.  
- The review also checks whether the drug can be manufactured consistently at high quality.

### Post-Approval Monitoring
Approval is not the end. After a drug is on the market:
- **Phase 4 studies** continue to monitor long-term safety and effectiveness.
- **Pharmacovigilance systems** collect reports of rare or unexpected side effects.
- Regulators may update labeling or restrict use if new risks are found.

> Regulatory review ensures that new medicines reaching patients are not only 
> effective but also safe, consistent, and trustworthy.
""")

module_keys = ["reg1","reg2","reg3","reg4","reg5"]
show_progress(module_keys)

st.subheader("Test your Knowledge")
quiz("The FDA submission for marketing approval is called…", 
    ["IND", "NDA", "BLA"], 1, "reg1")
quiz("Post-marketing surveillance is also called…", 
    ["Phase 4", "Phase 1", "Preclinical"], 0, "reg2")
quiz("A generic drug is…", 
    ["A brand-new molecule", "A cheaper equivalent after patent expiry", "Always less safe"], 1, "reg3")
quiz("The EMA regulates medicines in…", 
    ["United States", "Europe", "Japan"], 1, "reg4")
quiz("Pharmacovigilance refers to…", 
    ["Drug marketing", "Monitoring drug safety after approval", "Optimizing manufacturing"], 1, "reg5")

st.markdown("---")
st.write("button here")

