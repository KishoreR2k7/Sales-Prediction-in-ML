import streamlit as st
import pickle
import numpy as np
model,scaler=pickle.load(open('model.pkl','rb')),pickle.load(open('scaler.pkl','rb'))
st.title('Sales Prediction')
st.write("Enter the details below to predict.")
TV_spend=st.number_input('TV Spend')
radio_spend=st.number_input('Radio Spend')
social_spend=st.number_input('Social Media Spend')
features=np.array([[TV_spend,radio_spend,social_spend]])
features_scaled = scaler.transform(features)
if st.button("Predict Sales"):
    prediction=model.predict(features_scaled)
    st.success(f"Sales {prediction[0]:,.2f}k")