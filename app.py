# Streamlit UI
# import necessary libraries
import pickle
import pandas as pd
import numpy as np
import streamlit as st


# Model De-serialization (loading the model)
#  using pickle
# import pickle
with open("Linear_model.pkl","rb") as file:
    model = pickle.load(file)
# model.predict(data)

with open("label_encoder.pkl","rb") as file1:
    encoder = pickle.load(file1)


# # using joblib
# import joblib
# file = "model.pkl"
# model = joblib.load(file)
# # model.predict(data)


# load cleaned data
df = pd.read_csv("cleaned_data.csv")

st.set_page_config(page_title="house price prediction of Banglore",
                   page_icon="house_logo.jpeg")
with st.sidebar:
    st.title("Banglore House Price Prediction")
    st.image("house_logo.jpeg")


# input field
# Trained col seq: 'bhk','total_sqft','bath','encoded_loc'

location = st.selectbox("Location : ",options=df['location'].unique())
bhk = st.selectbox("BHK : ",options=sorted(df['bhk'].unique()))
sqft = st.number_input("Total sqft : ",min_value=300)
bath = st.selectbox("No. of Restrooms : ",options=sorted(df['bath'].unique()))

# encode the new location
encoded_loc = encoder.transform([location])
# st.write(encoded_loc)

# new data preparation
new_data = [[bhk,sqft,bath,encoded_loc[0]]]
# st.write(new_data)
# prediction
col1,col2 = st.columns([1,2])
if col2.button("Predict House Price"):
    pred = model.predict(new_data)[0]
    pred = round(pred*100000)
    st.subheader(f"Predicted Price : Rs.{pred}")