import pickle
import pandas as pd

with open("MODELS/student_performance_model.pkl", "rb") as file:
    model = pickle.load(file)

def predict_score(input_data):

    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)

    return float(prediction[0])