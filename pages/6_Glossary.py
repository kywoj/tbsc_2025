import streamlit as st

st.header("📖 Glossary of Key Terms in Drug Discovery & Development")

st.write("""
This glossary provides plain-language explanations of important terms you encountered in the course. Use it anytime you need a refresher.
""")

glossary = {
    "Assay": "A test to see how a compound affects a target.",
    "BLA (Biologics License Application)": "Approval request for a biologic product, like antibodies or vaccines.",
    "Clinical Trial": "A study in humans to check if a drug is safe and works.",
    "Hit": "A compound that shows some activity against a target.",
    "IND (Investigational New Drug)": "Application to start testing a drug in humans.",
    "Lead Compound": "A refined compound with better properties, ready for further testing.",
    "NDA (New Drug Application)": "Request to market a new drug in the U.S.",
    "Phase 1 Trial": "First human testing, focused on safety and dosage.",
    "Phase 2 Trial": "Testing in patients to see if the drug works and is safe.",
    "Phase 3 Trial": "Large trials to confirm effectiveness and monitor side effects.",
    "Pharmacodynamics (PD)": "What the drug does to the body.",
    "Pharmacokinetics (PK)": "What the body does to the drug (absorption, metabolism, excretion).",
    "Pharmacovigilance": "Monitoring drug safety after it’s on the market.",
    "Placebo": "An inactive substance used to compare effects in trials.",
    "Post-Marketing Surveillance": "Monitoring a drug’s safety and effectiveness after approval.",
    "Preclinical Studies": "Lab and animal tests before human trials.",
    "Regulatory Agency": "Official body (like FDA or EMA) that approves new medicines.",
    "Risk Management Plan (RMP)": "Plan to minimize and monitor risks of a medicine.",
    "Target": "A molecule in the body that a drug is designed to act on.",
    "Toxicology": "Study of harmful effects of drugs or chemicals.",
    "Drug Development Pipeline": "The full process from discovery to approval and beyond."
}


for term, definition in glossary.items():
    st.markdown(f"**{term}** — {definition}")


st.markdown("---")

