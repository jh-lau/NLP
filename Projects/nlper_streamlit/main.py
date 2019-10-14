"""
  User: Liujianhan
  Time: 10:42
 """
__author__ = 'liujianhan'

import sys
import json
import re
import time
import matplotlib.pyplot as plt
import matplotlib
import streamlit as st

import numpy as np
import pandas as pd
from ltp.extractor import Extractor

title_holder = st.empty()


def main():
    st.sidebar.header('Choice Feature to Use')
    st.write(f"[Baidu](http://www.baidu.com)", unsafe_allow_html=True)
    st.write("<h1>Helo h1", unsafe_allow_html=True)

    select_func = st.sidebar.selectbox('', ['Comment Extractor', 'Texts Summarization'])
    if select_func == 'Comment Extractor':
        comment_extractor(select_func)

    if select_func == 'Texts Summarization':
        text_summary(select_func)

    api_refer()


def comment_extractor(select_func):
    title_holder.markdown('# ' + select_func.split()[-1])
    comment = st.sidebar.text_input('Input your comment here')
    result = Extractor().sentence_parse(comment)
    st.write(result)

    if isinstance(result, tuple):
        df = pd.DataFrame(index=np.array(range(1)), columns=['Subject', 'Verb', 'Comment'])
        df.iloc[:, ] = result[0], result[1], result[2]
        st.write(df)


def text_summary(select_func):
    title_holder.markdown('# ' + select_func.split()[-1])
    summary = st.sidebar.text_area('Input your texts here', 'Texts need to be summarized.')
    st.write(summary)


def api_refer():
    st.sidebar.subheader('API Reference')
    result = st.sidebar.text_input('Input what would your like to search', 'np.eye')
    if result:
        module, *func = result.split('.')
        try:
            st.sidebar.help(eval(result))
        except Exception as e:
            st.sidebar.exception(f"No {e} is found, please try another one.")
    else:
        ''


if __name__ == '__main__':
    main()
