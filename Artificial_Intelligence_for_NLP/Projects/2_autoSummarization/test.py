import streamlit as st

st.sidebar.subheader("Component 1")

t1 = st.sidebar.text_input("Component 1 name")
s1 = st.sidebar.slider("Component 1 value")

st.sidebar.markdown("---")

st.sidebar.subheader("Component 2")
t2 = st.sidebar.text_area("")
s2 = st.sidebar.slider("Component 2")

st.title("Hello!")
st.write(t1, s1)
st.markdown('---')
def split_sentence(doc):
	sentence_split = doc.split('。')
	sen2index = {s:sentence_split.index(s) for s in sentence_split if s}
	index2sen = {k:v for v, k in sen2index.items()}
	return sen2index, index2sen

@st.cache
def fetch_data(filename):
	with open(filename, encoding='utf-8') as f:
		content = f.read()
	return content
	
content = fetch_data('data/news_demo.txt')
st.write(content)

t2,t2_ = split_sentence(content)

st.write(t2)
st.write(t2_)


st.markdown('---')
st.markdown('<style>h1{color: red;}</style>', unsafe_allow_html=True)

st.markdown('---')
st.markdown('<style>' + open('icon.css').read() + '</style>', unsafe_allow_html=True)
st.markdown('<i class="material-icons">In your face</i>', unsafe_allow_html=True)