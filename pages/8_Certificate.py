import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
from datetime import datetime
from utils import show_progress

if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = {}

st.header("🎓 Certificate of Completion")
show_progress()

total_questions = 25
answered_questions = len(st.session_state.answered)
overall_progress = answered_questions / total_questions
st.progress(overall_progress)
st.write(f"Overall Progress: {answered_questions}/{total_questions} questions answered")

if answered_questions < total_questions:
    st.warning("You need to complete all quizzes before receiving a certificate.")
else:
    st.success("🎉 Congratulations! You have completed all quizzes.")
    st.balloons()
    score = st.session_state.score
    st.write(f"Your final score: **{score}/25**")

    if score >= 15:
        st.success("You passed and earned your certificate!")
        name = st.text_input("Enter your name to appear on the certificate:", "")

        if name:
            date_str = datetime.today().strftime('%B %d, %Y')
            buffer = io.BytesIO()
            c = canvas.Canvas(buffer, pagesize=letter)
            width, height = letter
            c.setFont("Helvetica-Bold", 20)
            c.drawCentredString(width/2, height-100, "Certificate of Completion")
            c.setFont("Helvetica", 14)
            c.drawCentredString(width/2, height-150, "This certifies that")
            c.setFont("Helvetica-Bold", 16)
            c.drawCentredString(width/2, height-180, name)
            c.setFont("Helvetica", 14)
            c.drawCentredString(width/2, height-220, "has successfully completed the")
            c.drawCentredString(width/2, height-240, "Drug Discovery & Development Mini-Course")
            c.setFont("Helvetica", 12)
            c.drawCentredString(width/2, height-280, f"Final Score: {score}/25")
            c.drawCentredString(width/2, height-300, f"Date of Completion: {date_str}")
            c.setFont("Helvetica-Oblique", 10)
            c.drawCentredString(width/2, height-340, "Issued by Bruce 'The Corgi' Julian")
            c.showPage()
            c.save()
            buffer.seek(0)

            st.download_button(
                label="📥 Download Certificate (PDF)",
                data=buffer,
                file_name=f"certificate_{name.replace(' ', '_')}.pdf",
                mime="application/pdf"
            )
        else:
            st.info("Please enter your name above to generate your certificate.")
    else:
        st.error("Unfortunately, you did not meet the passing threshold (20/25). Please review the modules and try again.")
