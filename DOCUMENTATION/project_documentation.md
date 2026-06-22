# Student Performance Tracker Documentation

## Objective

The objective of this project is to predict student exam performance using machine learning techniques and various academic, behavioral, and personal factors.

---

## Problem Statement

Educational institutions often seek ways to identify factors influencing student performance. This project aims to analyze these factors and predict exam scores using machine learning models.

---

## Dataset Description

The dataset contains student-related information such as:

- Hours Studied
- Attendance
- Previous Scores
- Sleep Hours
- Tutoring Sessions
- Parental Involvement
- Teacher Quality
- Family Income
- Motivation Level
- Internet Access
- Extracurricular Activities
- School Type
- Gender

Target Variable:

- Exam Score

---

## Data Preprocessing

The following preprocessing steps were performed:

1. Missing value handling
2. Label Encoding of categorical features
3. Feature selection
4. Data cleaning
5. Train-test split

---

## Exploratory Data Analysis

Performed analyses include:

- Missing value analysis
- Exam score distribution
- Correlation heatmap
- Feature importance analysis
- Actual vs Predicted comparison

---

## Model Development

### Linear Regression

Performance:

- MAE: 1.02
- RMSE: 2.10
- R² Score: 0.689

### Random Forest Regressor

Performance:

- MAE: 1.13
- RMSE: 2.21
- R² Score: 0.655

Selected Model:

Linear Regression

Reason:

Linear Regression achieved a better R² score and lower prediction error compared to Random Forest.

---

## Streamlit Application

The application allows users to:

- Enter student-related information
- Predict exam scores
- View performance category

Performance Categories:

- Excellent
- Good
- Average
- Needs Improvement

---

## Results

The developed model successfully predicts student exam scores and provides performance categorization through an interactive web interface.

---

## Conclusion

The Student Performance Tracker demonstrates the complete machine learning workflow, including data preprocessing, model training, evaluation, and deployment using Streamlit.

---

## Future Scope

- Additional student features
- Real-time data integration
- Advanced machine learning models
- Performance analytics dashboard