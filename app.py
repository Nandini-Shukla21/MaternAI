import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load("maternAI_rf_model.pkl")       # Updated model file
scaler = joblib.load("maternAI_scaler.pkl")        # Scaler file

st.set_page_config(page_title="MaternAI - Pregnancy Risk Predictor", layout="centered")

st.title("🤰 MaternAI: Pregnancy Risk Level Prediction")
st.write("Enter the required medical parameters to assess pregnancy risk level.")

# UI Inputs
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=10, max_value=60, value=25)
    systolic_bp = st.number_input("Systolic BP (mm Hg)", min_value=70, max_value=200, value=120)
    diastolic_bp = st.number_input("Diastolic BP (mm Hg)", min_value=40, max_value=120, value=80)
    bs = st.number_input("Blood Sugar (BS)", min_value=0.0, max_value=20.0, value=5.0)
    body_temp = st.number_input("Body Temperature (°F)", min_value=95.0, max_value=105.0, value=98.6)

with col2:
    heart_rate = st.number_input("Heart Rate (bpm)", min_value=50, max_value=200, value=80)
    pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=15, value=1)
    complications = st.selectbox("Previous Complications", options=["No", "Yes"])
    hemoglobin = st.number_input("Hemoglobin (g/dL)", min_value=5.0, max_value=20.0, value=12.0)
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.0)

# Convert to numeric
complications = 1 if complications == "Yes" else 0

# Predict button
if st.button("Predict Risk Level"):
    # Prepare input
    input_data = np.array([[age, systolic_bp, diastolic_bp, bs, body_temp,
                            heart_rate, pregnancies, complications,
                            hemoglobin, bmi]])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)[0]

    # Output
    if prediction == 0:
        st.error("🔴 High Risk Pregnancy")
    else:
        st.success("🟢 Low Risk Pregnancy")
