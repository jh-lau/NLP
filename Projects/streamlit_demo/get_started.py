"""
  User: Liujianhan
  Time: 14:45
 """
__author__ = 'liujianhan'

import streamlit as st
import numpy as np
import pandas as pd
import time

st.title('My first app')

st.write("Here's our first attempt at using data to create a table:")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
    'third column': [100, 200, 300, 400]
})
df
# options = st.selectbox('Which number do you like best?', df['first column'])
# 'You selected:', options
option = st.sidebar.selectbox('Which number do you like best?', df['first column'])
'You selected:', option

if st.sidebar.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3), columns=list('abc')
    )
    st.line_chart(chart_data)
chart_data = pd.DataFrame(np.random.randint(1, 10, size=(20,3)), columns=list('ABC'))
st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000,2) / [50,50] + [24.46, 118.1],
    columns=['lat', 'lon'])
st.map(map_data)

'Starting a long computation...'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(.1)

'...and now we\'re done!'
