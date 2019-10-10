"""
  User: Liujianhan
  Time: 23:48
 """
__author__ = 'liujianhan'

import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt
# import seaborn as sns

st.title('This is a title')
st.header('This is a header')
st.subheader('This is a subheader')
st.text('This is plain text')
'# this should support markdown texts'
"`hello` world"
'Hello *World!*'
code = """
def hello():
    print("Hello Streamlit!")
"""
st.code(code, language='python')

df = pd.DataFrame({'first column': [1, 2, 3, 4],
            'second column': [10, 20, 30, 40]})

'1 + 1 = ', 2
'Below is a Dataframe'
df
'Above is a Dataframe.'

df2 = pd.DataFrame(np.random.randn(200, 3), columns=list('abc'))
c = alt.Chart(df2).mark_circle().encode(x='a', y='b', size='c', color='b')
c

df3 = pd.DataFrame(np.random.randn(10,20), columns=(f'col {i}' for i in range(20)))
st.dataframe(df3.style.highlight_max(axis=0))
# cm = sns.light_palette('green', as_cmap=True)
# df3.style.background_gradient(cmap=cm)
# st.write(dir(df3.style))
# arr = np.random.normal(1, 1, size=100)
# plt.hist(arr, bins=20)
# st.pyplot()

if st.button('Say hello'):
    'why hello there'
else:
    'Goodbye'

agree = st.checkbox('I agree')
if agree:
    'Great!'

genre = st.radio("what's your favorite movie genre",('Comedy', 'Drama', 'Documentary'))
if genre == 'Comedy':
    'You selected Comedy.'
else:
    f"You selected {genre}."

option = st.selectbox('How would you like to be contacted?',
                      ('Email', 'Home phone', 'Mobile phone'))
'You selected:', option


# options = st.multiselect(
#         'What are your favorite colors',
#         ('Green', 'Yellow', 'Red', 'Blue'),
#         ('Yellow', 'Red'))
# 'You selected:', options


age = st.slider('How old are you?', 0, 130, 25)
f"I'm {age} years old."

values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
'Values:', values

txt = st.text_area('Text to analyze', '''
...     It was the best of times, it was the worst of times, it was
...     the age of wisdom, it was the age of foolishness, it was
...     the epoch of belief, it was the epoch of incredulity, it
...     was the season of Light, it was the season of Darkness, it
...     was the spring of hope, it was the winter of despair, (...)
...     ''')
'Sentiment:', txt

import datetime
d = st.date_input('When is your birthday', datetime.date(2020,8,8))
'Your birthday is:',d

t = st.time_input('Set an alarm for', datetime.time(8,45))
'Alarm is set for', t

with st.echo():
    def hello():
        print('hello world')

# import time
# with st.spinner('Wait for it...'):
#     time.sleep(4)
# st.success('Done!')
# st.balloons()

st.error('This is an error')
st.warning('This is an warning')
st.info('This is info')
e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)

my_placeholder = st.empty()
my_placeholder.text('Hello world!')

st.set_option('a',1)