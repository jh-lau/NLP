"""
  User: Liujianhan
  Time: 14:36
  词性标注
 """
__author__ = 'liujianhan'

import jieba.posseg as pseg

string = "是广泛使用的中文分词工具，具有以下特点："
words = pseg.cut(string)
for word, flag in words:
    print(f"{word} {flag}")
