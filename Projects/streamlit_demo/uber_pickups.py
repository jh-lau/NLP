"""
  User: Liujianhan
  Time: 13:03
 """
__author__ = 'liujianhan'

import numpy as np
import pandas as pd
import streamlit as st

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'


@st.cache
def load_data(nrows):
    data = pd.read_csv('data/uber-raw-data-sep14.csv.gz', nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


data_load_state = st.text('Loading data...')
nrows = st.sidebar.selectbox('How many rows do you want to load?', range(1000, 10001, 1000))
data = load_data(nrows)
data_load_state.text('Loading data...done!')
# 'Done! (using cache)'

if st.sidebar.checkbox('Show raw data'):
    st.subheader('Raw data')
    data

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

st.subheader('Map of all pickups')
st.map(data)

hour_to_filter = st.sidebar.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)