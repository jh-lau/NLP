"""
  User: Liujianhan
  Time: 17:08
 """
import re
import jieba
import numpy as np
import jieba.posseg as pseg
from collections import defaultdict
from itertools import combinations
import networkx as nx
from sklearn.decomposition import TruncatedSVD
from gensim.models import fasttext

__author__ = 'liujianhan'


def word_weighted_prob(counter: dict, word, alpha=.001):
    denominator = sum(counter.values())
    try:
        prob = counter[word] / denominator
        weighted_prob = alpha / (alpha + prob)
    except KeyError:
        return 1.0
    return weighted_prob


def word_weighted_wv(counter, wv, word):
    word_vec = wv[word]
    word_prob = word_weighted_prob(counter, word)
    return word_prob * word_vec


def compute_pc(X, npc=1):
    svd = TruncatedSVD(n_components=npc, n_iter=7, random_state=0)
    svd.fit(X)
    return svd.components_


def remove_pc(X, npc=1):
    pc = compute_pc(X, npc)
    update_X = X - X @ (pc.T @ pc)
    return update_X


def sen2vec(sentences: list, counter, wv):
    result = []
    sen2vec_dict = defaultdict(int)
    for sentence in sentences:
        words = list(filter(lambda x: x.isalpha(), jieba.cut(sentence)))
        vs = sum([word_weighted_wv(counter, wv, word) for word in words])
        result.append(vs)
        sen2vec_dict[sentence] = vs
    assert len(result) == len(sentences)
    X = np.array(result)
    final_X = remove_pc(X)
    return final_X, sen2vec_dict


def split_sentence(doc):
    doc = re.sub(r'\s*', '', doc)
    doc = doc.replace('？', '。')
    doc = doc.replace('！', '。')
    result = doc.split('。')
    return result[:-1] if result[:-1] else result


def similarity_with_coocurr(s1, s2, jieba_cut=True):
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if jieba_cut:
        s1_words = list(filter(lambda x: x.isalnum(), list(jieba.cut(s1))))
        s2_words = list(filter(lambda x: x.isalnum(), list(jieba.cut(s2))))
    else:
        s1_words = list(s1)
        s2_words = list(s2)
    common_words = [word for word in s1_words if word in s2_words]
    numerator = len(common_words)
    denominator = np.log(len(s1_words)) + np.log(len(s2_words)) + .1
    return numerator / denominator


def get_sentences_edge(sentences: list, metrics, counter, wv):
    if len(sentences) == 1:
        return sentences

    if metrics.__name__ == 'cosine':
        _, sen2vec_dict = sen2vec(sentences, counter, wv)
        sentences = sen2vec_dict.keys()
        return [(s1, s2, metrics(sen2vec_dict[s1], sen2vec_dict[s2]))
                for (s1, s2) in list(combinations(sentences, 2))]
    return [(s1, s2, metrics(s1, s2))
            for (s1, s2) in list(combinations(sentences, 2))]


def summarize(sentences_with_edge, portion=.2):
    graph = nx.Graph()
    graph.add_weighted_edges_from(sentences_with_edge)
    rank = nx.pagerank(graph)
    sorted_rank = sorted(rank.items(), key=lambda x: x[1], reverse=True)
    summary_length = int(np.floor(len(graph.nodes) * portion))
    summary_length = summary_length if summary_length else 1
    result = [x[0] for x in sorted_rank[:summary_length]]
    return '；'.join(result) + '。'


def process_pipe(doc, metrics, counter, wv):
    split = split_sentence(doc)
    if len(split) == 1:
        return split[0] + '。'
    edges = get_sentences_edge(split, metrics, counter, wv)
    return summarize(edges)


def co_occurrence(doc, window_size=2):
    """
    Treat doc as a long sentence to extract keywords by textrank algorithm.
    :param doc:
    :param window_size:
    :return:
    """
    result = defaultdict(int)
    filtered = [word.word for word in pseg.cut(doc.replace(' ', ''))
                if word.flag in ['v', 'n'] if len(word.word) > 1]
    max_length = len(filtered)

    for i, word in enumerate(filtered):
        start = i - window_size if (i - window_size) > 0 else 0
        end = i + window_size + 1 if i + window_size + 1 < max_length else max_length
        candidates = filtered[start:end]
        candidates.remove(word)
        if candidates:
            for c in candidates:
                result[(word, c)] += 1
    return [(k[0], k[1], v) for k, v in result.items()]


def extract_keyword(co_list, topk=20):
    graph = nx.Graph()
    graph.add_weighted_edges_from(co_list)
    sorted_ = sorted(nx.pagerank(graph).items(), key=lambda x: x[1], reverse=True)[:topk]
    return [x[0] for x in sorted_]
