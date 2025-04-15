import streamlit as st
st.html("<h1 style='color: white;'>Diabetic and Non Diabetic Classifier</h1>")
import pickle
import string
import numpy as np

#Load model
try:
    model = pickle.load(open('model.pkl','rb'))
except FileNotFoundError as e:
    st.error(f"Error Loading the Model: {e}")
    st.stop
st.html("<p style='color: white;'>Please Provide the following information</p>")
#Input Message
preg = st.number_input("Enter the number of Pregnancy time", min_value=0, max_value=10)
glucose = st.number_input("Enter the Glucose Level")
bp = st.number_input("Enter BlooDiastolic blood pressure (mm Hg)")
skin = st.number_input("Enter Triceps skinfold thickness (mm)")
bmi = st.number_input("Enter Body mass index (weight in kg/height in m^2)")
dpf = st.number_input("Enter Diabetes pedigree function, a genetic score of diabetes.")
age = st.number_input("Enter your Age", min_value = 1,max_value= 100)
insulin = st.number_input("Enter 2-Hour serum insulin (mu U/ml).")

#Predict
if st.button("Predict"):
    input_data = np.array([[preg,glucose,bp,skin,bmi,dpf,age,insulin]])
    prediction = model.predict(input_data)
    #Display result
    if prediction == 1:
        st.header("Diabetic")
    else:
        st.header("Non Diabetic")