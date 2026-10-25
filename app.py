import streamlit as st
import pandas as pd
import joblib

model = joblib.load("heart_model.pkl")

st.title("Heart Disease Predictor")
st.write("Enter patient details to estimate heart disease risk.")

age = st.slider("Age", 20, 90, 50)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest pain type", ["typical angina", "atypical angina", "non-anginal", "asymptomatic"])
trestbps = st.number_input("Resting blood pressure", 80, 220, 120)
chol = st.number_input("Cholesterol", 0, 600, 200)
fbs = st.selectbox("Fasting blood sugar > 120", ["True", "False"])
restecg = st.selectbox("Resting ECG", ["normal", "lv hypertrophy", "st-t abnormality"])
thalch = st.number_input("Max heart rate", 60, 220, 150)
exang = st.selectbox("Exercise-induced angina", ["True", "False"])
oldpeak = st.number_input("ST depression (oldpeak)", 0.0, 7.0, 1.0)
slope = st.selectbox("ST slope", ["upsloping", "flat", "downsloping"])
ca = st.selectbox("Major vessels colored (0-3)", [0, 1, 2, 3])
thal = st.selectbox("Thal", ["normal", "fixed defect", "reversible defect"])

if st.button("Predict"):
    row = pd.DataFrame([{
        "age": age, "trestbps": trestbps, "chol": chol, "thalch": thalch,
        "oldpeak": oldpeak, "ca": ca, "sex": sex, "cp": cp, "fbs": fbs,
        "restecg": restecg, "exang": exang, "slope": slope, "thal": thal,
    }])
    prob = model.predict_proba(row)[0][1]
    st.metric("Risk probability", f"{prob*100:.1f}%")
    if prob > 0.5:
        st.error("Higher risk of heart disease")
    else:
        st.success("Lower risk of heart disease")
    st.caption("Educational project only, not medical advice.")