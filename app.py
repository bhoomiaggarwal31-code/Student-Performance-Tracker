import streamlit as st
from SRC.predict import predict_score
from SRC.utils import get_performance_category



st.title("🎓 Student Performance Tracker")

st.write("Predict Exam Score based on student factors")

# Inputs
hours_studied = st.slider("Hours Studied", 1, 50, 20)
attendance = st.slider("Attendance (%)", 50, 100, 75)
previous_scores = st.slider("Previous Score", 40, 100, 70)
sleep_hours = st.slider("Sleep Hours", 4, 12, 7)
tutoring_sessions = st.slider("Tutoring Sessions", 0, 10, 2)

if st.button("Predict Score"):

    input_data_dict = {
        "Hours_Studied": hours_studied,
        "Attendance": attendance,
        "Previous_Scores": previous_scores,
        "Sleep_Hours": sleep_hours,
        "Tutoring_Sessions": tutoring_sessions
    }

    score = predict_score(input_data_dict)

    category = get_performance_category(score)

    st.success(f"Predicted Exam Score: {score:.2f}")
    st.info(f"Performance Category: {category}")
