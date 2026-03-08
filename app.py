import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Churn Prediction Dashboard", layout="centered")

st.title("Customer Churn Prediction Dashboard")

st.write("Interactive tool to estimate customer churn risk.")

st.subheader("Customer Information")

tenure = st.slider("Tenure Months", 0, 72, 12)
monthly_charges = st.number_input("Monthly Charges", value=70.0)
total_charges = st.number_input("Total Charges", value=1000.0)

contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
dependents = st.selectbox("Dependents", ["Yes", "No"])

if st.button("Predict Churn"):

    model = joblib.load("xgb_model.pkl")

    input_data = pd.DataFrame(columns=model.get_booster().feature_names)
    input_data.loc[0] = 0

    input_data.loc[0, "Tenure Months"] = tenure
    input_data.loc[0, "Monthly Charges"] = monthly_charges
    input_data.loc[0, "Total Charges"] = total_charges

    if contract == "Two year":
        input_data.loc[0, "Contract_Two year"] = 1

    if dependents == "Yes":
        input_data.loc[0, "Dependents_Yes"] = 1

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    st.metric("Churn Probability", f"{probability:.2f}")

    st.progress(float(probability))

    if prediction == 1:
        st.error("High Churn Risk")
    else:
        st.success("Low Churn Risk")

    st.caption("Model: XGBoost | Interface built with Streamlit")