import streamlit as st
from utils import show_progress

# Initialize session state variables if they don't exist
if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = {}

# Main landing page content
st.title("🧬 Drug Discovery & Development for Designers")
st.write("""
Welcome to an interactive mini-course about the **drug discovery & development pipeline**, created with <3 especially for designers and other nonscientists.
""")

# Show overall progress and score in sidebar
show_progress()

st.markdown("---")
st.subheader("Course Overview")
st.markdown("""
 
This guide provides a clear, structured overview of how new medicines are discovered, tested, and brought to patients.  

You’ll learn through **five modules**:  
1. **Drug Discovery** – Finding and optimizing promising molecules  
2. **Preclinical Development** – Lab and animal testing to ensure safety  
3. **Clinical Development** – Human testing in Phases 1, 2, and 3  
4. **Regulatory & Commercialization** – Review and approval by agencies like the FDA or EMA  
5. **Post-Marketing Surveillance** – Monitoring safety and effectiveness in the real world  

At the end, you’ll reach a **Summary & Results page**, and you can review a **Glossary** of key terms anytime.  

Let’s get started! 🚀
            
""")

st.info("Use the left-hand sidebar to navigate between modules. Your progress and score will be tracked across all pages automatically.")

st.markdown("---")
st.subheader("Tips for Using the Course")
st.markdown("""
- The sidebar shows **overall progress** and **current score**.  
- Module-specific progress is displayed when you open a module.  
- If you want to reset progress, click **Rerun** in the top-right corner of the app.
- Complete all quizzes to unlock your certificate.  
- Please reach out to me with any feedback or questions: kylie.wojciechowski@merck.com
""")
