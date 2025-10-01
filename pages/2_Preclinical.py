import streamlit as st
from utils import quiz, show_progress

if "score" not in st.session_state:
     st.session_state.score = 0
if "answered" not in st.session_state:
     st.session_state.answered = {}

st.session_state.current_module = "Preclinical"

st.header("2. Preclinical Development")
st.write("""
Once researchers have selected the most promising compound from discovery, 
it cannot go directly into human testing. The next step is the **preclinical phase**, 
where scientists run a series of experiments in the lab and in animals to 
answer a critical question:

**Is this drug candidate reasonably safe and effective enough to test in humans?**

### Goals of Preclinical Research
- **Understand safety risks:** Before involving people, scientists must rule out 
compounds that could be toxic or harmful.
- **Understand how the drug behaves in the body:** How is it absorbed, distributed, 
broken down (metabolized), and eliminated? This is called **pharmacokinetics (PK)**.
- **Understand what the drug does to the body:** What is its biological effect? 
This is called **pharmacodynamics (PD)**.

### Types of Preclinical Studies
- **Toxicology studies**: Identify harmful side effects at different doses.
- **Dose range finding**: Establish the safe starting dose for human trials.
- **Pharmacokinetics (PK)**: Study absorption, distribution, metabolism, and excretion.
- **Pharmacodynamics (PD)**: Measure how the drug affects its biological target.

### Standards and Regulation
All preclinical studies must follow **Good Laboratory Practice (GLP)** standards.  
The results are compiled into an **Investigational New Drug (IND)** application, 
which is submitted to the FDA (or other regulators).  
Only after the IND is reviewed and accepted can clinical trials in humans begin.
""")

module_keys = ["pre1","pre2","pre3","pre4","pre5"]
show_progress(module_keys)

st.subheader("Test your Knowledge")
quiz("Preclinical studies are conducted in…", 
     ["Humans", "Animals and cell systems", "Computers only"], 1, "pre1")
quiz("The study of what the body does to a drug is called…", 
     ["Pharmacodynamics", "Pharmacokinetics", "Toxicology"], 1, "pre2")
quiz("GLP stands for…", 
     ["Good Laboratory Practice", "Great Lab Processes", "General Licensing Protocol"], 0, "pre3")
quiz("A toxicology study measures…", 
     ["How the drug is metabolized", "Potential harmful effects", "The drug price"], 1, "pre4")
quiz("An IND application is filed…", 
     ["Before clinical trials", "After FDA approval", "During sales launch"], 0, "pre5")

st.markdown("---")
st.write("button here")

