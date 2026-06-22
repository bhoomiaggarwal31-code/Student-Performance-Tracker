# Student Performance Tracker

## Intern Details

* **Intern ID:** CITS4532
* **Full Name:** Bhoomi Aggarwal
* **Duration:** 6 Weeks

---

## Project Name

Student Performance Tracker

---

## Project Scope

The Student Performance Tracker is a Machine Learning project developed to predict a student's exam score based on various academic and behavioral factors.

The project uses data analysis, preprocessing techniques, machine learning algorithms, and a Streamlit-based web application to provide score predictions. The objective is to identify key factors affecting student performance and build an interactive prediction system.

---

## Features

* Exploratory Data Analysis (EDA)
* Missing Value Handling
* Feature Encoding
* Model Training and Evaluation
* Student Score Prediction
* Performance Category Classification
* Interactive Streamlit Web Application

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Streamlit
* Git & GitHub

---

## Machine Learning Models

### Linear Regression

Performance Metrics:

* MAE: 1.0155
* RMSE: 2.0974
* R² Score: 0.6888

### Random Forest Regressor

Performance Metrics:

* MAE: 1.1314
* RMSE: 2.2095
* R² Score: 0.6546

### Selected Model

Linear Regression was selected as the final model because it achieved better predictive performance than Random Forest on the dataset.

---

## Project Structure

Student-Performance-Tracker/

├── DATA/

├── DOCUMENTATION/

├── MODELS/

├── NOTEBOOKS/

├── OUTPUTS/

├── SCREENSHOTS/

├── SRC/

├── app.py

├── requirements.txt

├── README.md

└── .gitignore

---

## Screenshots

### Main Application Interface

<img width="1701" height="845" alt="main_ui" src="https://github.com/user-attachments/assets/c520f625-b7ac-4301-9cb7-5cf9dd2bc2e1" />


### User Input Screen

<img width="1442" height="833" alt="input_values" src="https://github.com/user-attachments/assets/86d74cd0-6690-4c69-9b88-8a315001a6a9" />


### Prediction Output

<img width="1533" height="824" alt="prediction_result" src="https://github.com/user-attachments/assets/6760d127-1679-4cfd-aa71-bcaaf40e63f5" />


### Model Comparison

<img width="1600" height="900" alt="model_comparsion" src="https://github.com/user-attachments/assets/627c5eb2-1cf3-4cb9-8642-49eb58c44fd8" />


---

## Output Visualizations

* Exam Score Distribution
* Correlation Heatmap
* Encoded Correlation Heatmap
* Feature Importance Plot
* Actual vs Predicted Scores Plot

---

## Installation

1. Clone the repository

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the application

```bash
python -m streamlit run app.py
```

---

## Future Enhancements

* Support additional student performance factors
* Deploy application on Streamlit Cloud
* Add data visualization dashboard
* Enable batch prediction using CSV uploads

---

## Conclusion

This project demonstrates the complete Machine Learning workflow, including data preprocessing, exploratory data analysis, model training, model evaluation, and deployment through a Streamlit web application. The final system provides accurate exam score predictions and helps analyze the factors influencing student performance.
