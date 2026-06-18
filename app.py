import streamlit as st
import pickle
import pandas as pd

# Load Model
with open("MODELS/student_performance_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🎓 Student Performance Tracker")

st.write("Predict Exam Score based on student factors")

# Inputs
hours_studied = st.slider("Hours Studied", 1, 50, 20)
attendance = st.slider("Attendance (%)", 50, 100, 75)
previous_scores = st.slider("Previous Score", 40, 100, 70)
sleep_hours = st.slider("Sleep Hours", 4, 12, 7)
tutoring_sessions = st.slider("Tutoring Sessions", 0, 10, 2)

if st.button("Predict Score"):

    input_data = pd.DataFrame({
        "Hours_Studied": [hours_studied],
        "Attendance": [attendance],
        "Previous_Scores": [previous_scores],
        "Sleep_Hours": [sleep_hours],
        "Tutoring_Sessions": [tutoring_sessions]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted Exam Score: {prediction[0]:.2f}")