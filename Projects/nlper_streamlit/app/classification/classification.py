"""
  User: Liujianhan
  Time: 15:18
 """
__author__ = 'liujianhan'
import streamlit as st


def comment_classification(select_func, title_holder):
    title_holder.markdown('# ' + select_func.split()[-1].upper())
    classified = st.sidebar.text_area('Input your texts here', 'Texts need to be classified.')
    st.write(classified)
