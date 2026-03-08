# Churn Deployment Framework

A lightweight machine learning deployment framework for customer churn prediction with explainable AI support.

## Overview

This repository contains a complete pipeline for customer churn prediction using an XGBoost model and an interactive Streamlit dashboard. The framework integrates machine learning modelling with explainability techniques using SHAP to support transparent decision-making.

## Features

- Customer churn prediction using XGBoost
- Model interpretability using SHAP values
- Interactive dashboard built with Streamlit
- Lightweight deployment for rapid experimentation
- Reproducible research framework

## Repository Structure

churn-deployment/

app.py – Streamlit application  
xgb_model.pkl – trained XGBoost model  
telco_.xlsx – dataset used for evaluation  
requirements.txt – Python dependencies  
README.md – documentation  

## Installation

Clone the repository:

Install dependencies:

pip install -r requirements.txt

## Run the Dashboard

Launch the Streamlit application:

The dashboard will open in the browser and allow users to explore churn predictions and SHAP explanations.

## Dataset

The framework uses the Telco Customer Churn dataset for demonstration purposes.

## License

MIT License

## Contact

For questions or issues, please contact:
somilabopopoola@gmail.com

streamlit run app.py