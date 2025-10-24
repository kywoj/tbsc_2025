import streamlit as st

if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = {}

st.header("🎉 Course Summary")
st.write("""
Congratulations on completing the mini-course! You’ve now explored the full journey of how medicines are discovered, tested, and approved:

1. **Drug Discovery** – Identifying and optimizing potential drug candidates.  
2. **Preclinical Development** – Testing in the lab and in animals to gather safety data.  
3. **Clinical Development** – Running human trials across Phases 1, 2, and 3.  
4. **Regulatory & Commercialization** – Submitting data for approval by agencies like the FDA or EMA.  
5. **Post-Marketing Surveillance** – Monitoring real-world use, safety, and effectiveness.  

Each step is essential to ensure that new treatments are **safe, effective, and trustworthy**.
""")

# Calculate results
total_questions = 25
#total_questions = len(st.session_state.answered)

score = st.session_state.score

st.subheader("📊 Your Results")
st.write(f"**Final Score:** {score} out of {total_questions}")

# Feedback message
if score == total_questions:
    st.success("Outstanding! 🌟 You answered every question correctly.")
elif score > total_questions * 0.7:
    st.success("Great job! 👍 You have a strong grasp of the drug development process.")
elif score > total_questions * 0.5:
    st.info("Good effort! Keep reviewing the modules to strengthen your understanding.")
elif score == 0:
    st.info("You didn't finish! Go back and take your best shot at answering all the questions in each module.")
else:
    st.warning("Don’t worry, this is a tough topic. Try revisiting the modules and quizzes.")

st.markdown("---")

if score != 0:
    st.write("Thank you for taking this mini-course! Don't forget to download your certificate on the next page. ")