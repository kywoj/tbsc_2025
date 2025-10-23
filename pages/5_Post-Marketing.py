import streamlit as st
from utils import quiz, show_progress

if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = {}

st.session_state.current_module = "Post-Marketing"

st.header("5. Post-Marketing Surveillance (Phase IV)")
st.write("""
Even after regulatory approval, the work is not finished. 
Drugs must be monitored continuously to ensure they remain safe and effective in the real world.

This stage is often referred to as **post-marketing surveillance** or **Phase 4 studies**.

### Why Post-Marketing Matters
- **Real-world populations**: Clinical trials often involve carefully selected patients. 
  Once a drug is approved, it may be used in much larger and more diverse groups, 
  including people with multiple conditions or who take other medications.
- **Rare side effects**: Large populations make it easier to detect very rare 
  adverse effects that would not have appeared in smaller trials.
- **Long-term safety and effectiveness**: Some effects only emerge after 
  years of widespread use.

### Key Activities
- **Pharmacovigilance systems**: Regulators, health systems, and manufacturers 
  collect reports of adverse drug events.
- **Phase 4 clinical trials**: Additional studies may be required to explore 
  safety in specific populations (children, elderly, pregnant patients).
- **Risk Management Plans (RMPs)**: Companies may implement strategies to minimize 
  risks, such as special labeling or restricted distribution.
- **Label updates**: If new data emerges, drug labeling may be revised 
  to add warnings, precautions, or expanded indications.

Post-marketing surveillance ensures that patient safety continues  to be the top priority even after a drug is on pharmacy shelves.
""")

module_keys = ["post1","post2","post3","post4","post5"]
show_progress(module_keys)

st.subheader("Test your Knowledge")
quiz("Phase 4 studies occur…", 
     ["Before approval", "After approval", "Only during manufacturing"], 1, "post1")

quiz("One main purpose of post-marketing surveillance is to…", 
     ["Test advertising effectiveness", "Detect rare side effects", "Speed up approvals"], 1, "post2")

quiz("Pharmacovigilance refers to…", 
     ["Monitoring safety after approval", "Designing new molecules", "Recruiting trial volunteers"], 0, "post3")

quiz("Why might drug labeling be updated post-approval?", 
     ["To reflect new safety or effectiveness data", "To improve marketing slogans", "To change drug prices"], 0, "post4")

quiz("Risk Management Plans (RMPs) are used to…", 
     ["Minimize risks and guide safe use", "Negotiate insurance coverage", "Expand advertising"], 0, "post5")

st.markdown("---")
