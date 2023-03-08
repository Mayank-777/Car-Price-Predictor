import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('Random_Forest_Regressor.pkl', 'rb'))

st.header('Car Price Predictor')

Year = st.selectbox('Year Of Buying(enter only till 2019)',[1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019])
Present_Price = st.number_input('Present Price(in Lakhs)')
Kms_Driven = st.number_input('Kilometer Driven')
Kms_Driven2 = np.log(Kms_Driven)
Owner = st.selectbox('Number Of Previous Owners',[0,1,3])
Fuel_Type_Petrol = st.selectbox('Fuel Type',['Petrol','Diesel','CNG'])
if (Fuel_Type_Petrol == 'Petrol'):
    Fuel_Type_Petrol = 1
    Fuel_Type_Diesel = 0
elif (Fuel_Type_Petrol == 'Diesel'):
    Fuel_Type_Petrol = 0
    Fuel_Type_Diesel = 1
else:
    Fuel_Type_Petrol = 0
    Fuel_Type_Diesel = 0
Year = 2023 - Year
Seller_Type_Individual = st.selectbox('Seller Type',['Individual','Dealer'])
if (Seller_Type_Individual == 'Individual'):
    Seller_Type_Individual = 1
else:
    Seller_Type_Individual = 0
Transmission_Mannual = st.selectbox('Transmission Type',['Mannual','Automatic'])
if (Transmission_Mannual == 'Mannual'):
    Transmission_Mannual = 1
else:
    Transmission_Mannual = 0
if st.button('Predict Price'):
    query = np.array([Present_Price, Kms_Driven2, Owner, Year, Fuel_Type_Diesel, Fuel_Type_Petrol,Seller_Type_Individual, Transmission_Mannual])
    query = query.reshape(1,8)
    prediction = model.predict(query)[0]
    st.header("The Predicted Price of this Car is " + str(int(model.predict(query)[0])) + " Lakhs")