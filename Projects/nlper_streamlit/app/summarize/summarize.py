"""
  User: Liujianhan
  Time: 15:17
 """
from scipy.spatial.distance import cosine

__author__ = 'liujianhan'
import streamlit as st
import json
from bokeh.models import HoverTool
from bokeh.plotting import figure
from jieba.analyse import textrank, extract_tags
from .config import FASTTEXT_KEYED_VECTOR
from gensim.models import KeyedVectors
from gensim.summarization.summarizer import summarize as gensim_summarize
from .utils import *

news_demo = """
从习近平主席的贺信中，可以看出我们有信心，推动互联网发挥更好的影响和更大的作用。”中国工程院院士邬贺铨表示，今年适逢互联网诞生50周年、中国全功能接入互联网25周年，互联网行业持续蓬勃发展，中国将大有可为。
“习近平主席的贺信对世界互联网行业的发展提出了殷切希望，再次鼓舞中国互联网企业家们投身到数字中国的建设中去。”快手科技创始人兼首席执行官宿华说，得益于国家在互联网基础设施上的巨大投入，快手等一大批科技企业快速成长，见证、记录着国家日新月异的发展进程。
“中国数字经济蓬勃发展，正成为创新经济发展方式的新引擎。信息技术为制造业、商业等各行各业有效赋能，推动国家不断前进。”全国工商联副主席、正泰集团董事长南存辉说，公司深耕制造业数字化转型升级，努力探索物联网技术与智慧能源的深度融合之路。
杭州大搜车集团首席执行官姚军红说，当前传统汽车行业进入深度调整期，流通市场急需变革，以降低车辆消费门槛，提振消费市场信心。大搜车采用人工智能、大数据等技术，建立开放平台，精准对接传统工厂、商家和客户，为消费者带来切实利益。
旷视科技联合创始人兼首席执行官印奇说，新一轮互联网科技革命和产业变革加速演进，让从业者深切感受到机遇与挑战并存。印奇表示，旷视始终坚持自主创新，已成为全球为数不多的拥有自主研发深度学习框架的公司之一，将努力帮助中国企业在人工智能时代来临时，成为引领世界的力量。
“习近平主席在贺信中强调了人工智能、大数据、物联网等新技术新应用新业态方兴未艾，互联网迎来了更加强劲的发展动能和更加广阔的发展空间。这让我们对抢抓新机遇、拥抱数字化，推动产业升级的道路充满信心。”绍兴市委常委、诸暨市委书记徐良平说。
徐良平介绍，诸暨拥有4家省级工业互联网平台，还将针对袜业、珍珠、铜加工三大主导产业企业的数字化改造进行专项政策扶持。
"""


# todo OOV problem
# word2vec = Word2Vec.load(WORD2VEC_KEYED_VECTOR)

@st.cache
def fetch_data(vector_path, token_path):
    fasttext_ = KeyedVectors.load(vector_path)
    with open(token_path, 'r', encoding='utf-8') as f:
        tokens_counter_ = json.load(f)
    return fasttext_, tokens_counter_


fasttext, tokens_counter = fetch_data(FASTTEXT_KEYED_VECTOR, 'data/tokens_counter.json')


def pretty_output(doc, kw):
    color = ['green', 'red', 'blue', 'plum', 'sienna', 'yellowgreen', 'tan', 'maroon', 'salmon', 'grey']
    doc = doc.replace(' ', '')
    for i, k in enumerate(kw):
        replacer = f"<font color={color[i]}>{k}</font>"
        doc = doc.replace(k, replacer)
    return doc


def text_summary(select_func, title_holder):
    title_holder.markdown('# ' + select_func.split()[-1].upper())
    st.info('Raw content')
    raw_content = st.empty()
    demo_checkbox = st.sidebar.checkbox('Show news demo')

    st.sidebar.subheader('Input your texts here')
    content = st.sidebar.text_area('Click outside textarea after input', 'Texts need to be summarized.')

    st.sidebar.subheader('Method to compute similarity')
    metric_radio = st.sidebar.radio('', ('Co-occur', 'Cosine'))
    if metric_radio == 'Cosine':
        metric = cosine
        st.sidebar.selectbox('Method to compute sentence embedding',
                             ('SIF', 'Average Embedding'))
    else:
        metric = similarity_with_coocurr

    if demo_checkbox:
        content = news_demo

    if content != 'Texts need to be summarized.':
        raw_content.markdown(content)
        summary = process_pipe(content, metric, tokens_counter, fasttext)
        st.success(f'Summarized content with {metric.__name__}')
        st.write(summary)

        st.warning(f'Summarized content with gensim API - Unstable')
        try:
            st.write(gensim_summarize(content))
        except ValueError as e:
            st.error(e)

    st.sidebar.subheader('Keywords')
    show_kw = st.sidebar.checkbox('Show Keywords')
    if show_kw:
        kw_length = st.sidebar.slider(label='Keywords Number', min_value=3, max_value=10)
        kw_method = st.sidebar.selectbox('Method to extract keywords',
                                         ('TextRank', 'TextRank API', 'Tf-idf API'))
        if kw_method == 'TextRank':
            keywords = extract_keyword(co_occurrence(content, window_size=2), topk=kw_length)
        elif kw_method == 'TextRank API':
            keywords = textrank(content, topK=kw_length)
        else:
            keywords = extract_tags(content, topK=kw_length)
        st.sidebar.info('\t'.join(keywords))

        content = pretty_output(content, keywords)
    raw_content.markdown(content, unsafe_allow_html=True)
    # bokeh_figure()


def bokeh_figure():
    n = 500
    x = 2 + 2 * np.random.standard_normal(n)
    y = 2 + 2 * np.random.standard_normal(n)

    p = figure(title="Hexbin for 500 points", match_aspect=True,
               tools="wheel_zoom,reset", background_fill_color='#440154')
    p.grid.visible = False

    r, bins = p.hexbin(x, y, size=0.5, hover_color="pink", hover_alpha=0.8)

    p.circle(x, y, color="white", size=1)

    p.add_tools(HoverTool(
        tooltips=[("count", "@c"), ("(q,r)", "(@q, @r)")],
        mode="mouse", point_policy="follow_mouse", renderers=[r]
    ))
    st.bokeh_chart(p)
