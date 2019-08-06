"""
  User: Liujianhan
  Time: 19:48
 """
import random

__author__ = 'liujianhan'
import jieba
from collections import Counter


def cut(string):
    return list(jieba.cut(string))


TOKEN = []
for _, line in enumerate((open('article_9k.txt', encoding='utf-8'))):
    # if _ % 1000 == 0:
    #     print(_)
    if _ > 5000:
        break
    TOKEN += cut(line)


def create_grammar(grammar_str, split='=>', line_split='\n'):
    grammar = {}
    for line in grammar_str.split(line_split):
        if not line.strip():
            continue
        exp, stmt = line.split(split)
        grammar[exp.strip()] = [s.split() for s in stmt.split('|')]
    return grammar


def generate(gram, target):
    if target not in gram:
        return target
    expanded = [generate(gram, t) for t in random.choice(gram[target])]
    return ''.join([e if e != '/n' else '\n' for e in expanded if e != 'null'])


words_count = Counter(TOKEN)
TOKEN = [str(t) for t in TOKEN]
TOKEN_2_GRAM = [''.join(TOKEN[i:i + 2]) for i in range(len(TOKEN[:-2]))]
words_count_2 = Counter(TOKEN_2_GRAM)


def prob_1(word):
    return words_count[word] / len(TOKEN)


def prob_2(word1, word2):
    if word1 + word2 in words_count_2:
        return words_count_2[word1 + word2] / len(TOKEN_2_GRAM)
    else:
        return 1 / len(TOKEN_2_GRAM)


def prob_2_2(word1, word2):
    if word1 + word2 in words_count_2:
        return words_count_2[word1 + word2] / Counter(TOKEN)[word1]
    else:
        return 1 / len(TOKEN_2_GRAM)


def get_probability(sentence):
    words = cut(sentence)
    sentence_pro = 1
    for _, word in enumerate(words[:-1]):
        next_ = words[_ + 1]
        probability = prob_2(word, next_)
        sentence_pro *= probability
    return sentence_pro


def get_probability_2(sentence):
    words = cut(sentence)
    sentence_pro = 1
    for _, word in enumerate(words[:-1]):
        next_ = words[_ + 1]
        probability = prob_2_2(word, next_)
        sentence_pro *= probability
    return sentence_pro


# need_compared = [
#     "今天晚上请你吃大餐，我们一起吃日料 明天晚上请你吃大餐，我们一起吃苹果",
#     "真事一只好看的小猫 真是一只好看的小猫",
#     "今晚我去吃火锅 今晚火锅去吃我",
#     "洋葱奶昔来一杯 养乐多绿来一杯"
# ]
#
# for s in need_compared:
#     s1, s2 = s.split()
#     p1, p2 = get_probability(s1), get_probability(s2)
#
#     better = s1 if p1 > p2 else s2
#     print(f"{better} is more possible.")
#     print(f"{'-' * 4} {s1} with probability {p1}")
#     print(f"{'-' * 4} {s2} with probability {p2}")

if __name__ == '__main__':
    # print(prob_2('我们', '在'))
    # print(prob_2_2('我们', '在'))
    print(get_probability('我们在哪儿啊呀呀'))
    print(get_probability_2('我们在哪儿啊呀呀'))

