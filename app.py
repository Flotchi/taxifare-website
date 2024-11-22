import streamlit as st
import requests

st.markdown('Hello')

pickup_datetime = st.text_input('Date', '')
pickup_longitude = st.text_input('pickup_longitude', '')
pickup_latitude = st.text_input('pickup_latitude', '')
dropoff_longitude = st.text_input('dropoff_longitude', '')
dropoff_latitude = st.text_input('dropoff_latitude', '')
passenger_count = st.text_input('passenger_count', '')

url = 'https://taxifare.lewagon.ai/predict'

params = {'pickup_datetime':pickup_datetime,'pickup_longitude':pickup_longitude,'pickup_latitude':pickup_latitude,'dropoff_longitude':dropoff_longitude,'dropoff_latitude':dropoff_latitude, 'passenger_count':passenger_count}

response = requests.get(url, params=params).json()

st.write('Fare =', response['fare'])
