import streamlit as st
import requests
import pandas as pd
import datetime

st.markdown('Hello')

date = st.date_input(
    "select a date",
    datetime.date(2024, 7, 6))
time = st.time_input('Selec a time', datetime.time(8, 45))
pickup_datetime = f'{date} {time}'
pickup_longitude = st.text_input('pickup_longitude', '')
pickup_latitude = st.text_input('pickup_latitude', '')
dropoff_longitude = st.text_input('dropoff_longitude', '')
dropoff_latitude = st.text_input('dropoff_latitude', '')
passenger_count = st.text_input('passenger_count', '')

url = 'https://taxifare.lewagon.ai/predict'

params = {'pickup_datetime':pickup_datetime,'pickup_longitude':pickup_longitude,'pickup_latitude':pickup_latitude,'dropoff_longitude':dropoff_longitude,'dropoff_latitude':dropoff_latitude, 'passenger_count':passenger_count}

response = requests.get(url, params=params).json()

st.write('Fare =', response['fare'])

def get_map_data():
    return pd.DataFrame(
        {'lat': [float(pickup_latitude), float(dropoff_latitude)],
         'lon': [float(pickup_longitude), float(dropoff_longitude)]}
    )

df = get_map_data()

st.map(df)
