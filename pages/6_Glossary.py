import streamlit as st

st.header("📖 Glossary of Key Terms in Drug Discovery & Development")

st.write("""
This glossary provides plain-language explanations of important terms you encountered in the course.  
Use it anytime you need a refresher.
""")

glossary = {
    "Assay": "test",
    "Target": "A biological molecule (such as a protein, receptor, or enzyme) that a drug is designed to act on.",
    "Hit": "A compound that shows initial activity against a biological target during screening.",
    "Lead Compound": "A promising chemical or biological molecule refined from hits to have better properties as a potential drug.",
    "Preclinical Studies": "Lab and animal tests conducted before human trials to evaluate safety and biological activity.",
    "IND (Investigational New Drug)": "An application submitted to regulators (like the FDA) to begin testing a drug in humans.",
    "Phase 1 Trial": "The first stage of human testing, focused mainly on safety and dosage in healthy volunteers.",
    "Phase 2 Trial": "Mid-stage testing in patients with the disease to evaluate effectiveness and side effects.",
    "Phase 3 Trial": "Large-scale trials to confirm effectiveness, monitor side effects, and compare against standard treatments.",
    "NDA (New Drug Application)": "A request to the FDA for approval to market a new drug in the U.S.",
    "BLA (Biologics License Application)": "A request for approval to market a biologic product (like antibodies or vaccines).",
    "Regulatory Agency": "An official body (like the FDA in the U.S. or EMA in Europe) that evaluates and approves new medicines.",
    "Pharmacovigilance": "The practice of monitoring and studying the safety of drugs once they are on the market.",
    "Post-Marketing Surveillance": "Ongoing monitoring of a drug’s safety and effectiveness after approval, also called Phase 4 studies.",
    "Risk Management Plan (RMP)": "A formal strategy to minimize and monitor the risks of a medicine once it is in use.",
    "Placebo": "An inactive substance designed to look like the real drug, used in trials to compare effects."
}

for term, definition in glossary.items():
    st.markdown(f"**{term}** — {definition}")


st.markdown("---")
st.write("button here")

