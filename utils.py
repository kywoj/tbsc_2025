import streamlit as st

def quiz(question, options, correct, key):
    """
    Display a multiple-choice question with a submit button.
    No option is pre-selected. Feedback is shown only after submission.
    """

    # Ensure session state variables exist
    if "answered" not in st.session_state:
        st.session_state.answered = {}
    if "score" not in st.session_state:
        st.session_state.score = 0

    # If already answered, show question and result
    if key in st.session_state.answered:
        st.write(f"**Q:** {question}")
        user_ans = st.session_state.answered[key]
        if user_ans == options[correct]:
            st.success(f"You answered: {user_ans} ✅ Correct")
        else:
            st.error(f"You answered: {user_ans} ❌ Incorrect. Correct answer: {options[correct]}")
        return

    # Add a placeholder at the start of options
    display_options = ["-- Select an answer --"] + options
    ans = st.radio(question, display_options, index=0, key=f"radio_{key}")

    # Only allow submission if user selected a real answer
    if ans != "-- Select an answer --":
        if st.button("Submit", key=f"submit_{key}"):
            if ans == options[correct]:
                st.success("Correct! ✅")
                st.session_state.score += 1
            else:
                st.error(f"Incorrect ❌. Correct answer: {options[correct]}")
            st.session_state.answered[key] = ans

def show_progress(module_keys=None):
    """
    Display overall and module-specific progress in the sidebar.

    Parameters:
    - module_keys: list of str, keys for questions in the current module (optional)
    """

    # Ensure session state variables exist
    if "answered" not in st.session_state:
        st.session_state.answered = {}
    if "score" not in st.session_state:
        st.session_state.score = 0

    total_questions = 25
    answered_questions = len(st.session_state.answered)
    overall_progress = answered_questions / total_questions if total_questions > 0 else 0

    st.sidebar.title("📊 Progress Tracker")
    st.sidebar.progress(overall_progress)
    st.sidebar.write(f"Overall Progress: {answered_questions}/{total_questions} questions answered")
    st.sidebar.metric("Current Score", st.session_state.score)

    if module_keys:
        module_answered = sum(1 for k in module_keys if k in st.session_state.answered)
        st.sidebar.write(f"Module Progress: {module_answered}/{len(module_keys)} questions answered")
