"""
  User: Liujianhan
  Time: 15:07
 """
__author__ = 'liujianhan'
import sys
import streamlit as st
import pandas as pd
import numpy as np
import plotly
import plotly.express as px
import plotly.graph_objs as go
import plotly.io as pio


def comment_extractor(select_func, title_holder):
    title_holder.markdown('# ' + select_func.split()[-1].upper())
    comment = st.sidebar.text_input('Input your comment here')
    result = comment
    st.write(result)
    plotly_figure()

    if isinstance(result, tuple):
        df = pd.DataFrame(index=np.array(range(1)), columns=['Subject', 'Verb', 'Comment'])
        df.iloc[:, ] = result[0], result[1], result[2]
        st.write(df)


def plotly_figure():
    wind = px.data.wind()
    fig = px.bar_polar(wind, r="frequency", theta="direction",
                       color="strength", template="plotly_dark",
                       color_discrete_sequence=px.colors.sequential.Plasma[-2::-1])
    st.plotly_chart(fig)

    fig = go.Figure()
    fig.add_trace(go.Barpolar(
        r=[77.5, 72.5, 70.0, 45.0, 22.5, 42.5, 40.0, 62.5],
        name='11-14 m/s',
        marker_color='rgb(106,81,163)'
    ))
    fig.add_trace(go.Barpolar(
        r=[57.5, 50.0, 45.0, 35.0, 20.0, 22.5, 37.5, 55.0],
        name='8-11 m/s',
        marker_color='rgb(158,154,200)'
    ))
    fig.add_trace(go.Barpolar(
        r=[40.0, 30.0, 30.0, 35.0, 7.5, 7.5, 32.5, 40.0],
        name='5-8 m/s',
        marker_color='rgb(203,201,226)'
    ))
    fig.add_trace(go.Barpolar(
        r=[20.0, 7.5, 15.0, 22.5, 2.5, 2.5, 12.5, 22.5],
        name='< 5 m/s',
        marker_color='rgb(242,240,247)'
    ))

    fig.update_traces(text=['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'])
    fig.update_layout(
        title='Wind Speed Distribution in Laurel, NE',
        font_size=16,
        legend_font_size=16,
        polar_radialaxis_ticksuffix='%',
        polar_angularaxis_rotation=90,

    )
    st.plotly_chart(fig)
