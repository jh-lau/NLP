"""
  User: Liujianhan
  Time: 0:11
 """
__author__ = 'liujianhan'

from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'C:\Users\Administrator\Anaconda3\stanfordnlp', lang='zh')

fin = open('news.txt', 'r', encoding='utf-8')
fner = open('ner.txt', 'w', encoding='utf-8')
ftag = open('pos_tag.txt', 'w', encoding='utf-8')
for line in fin:
    line = line.strip()
    if len(line) < 1:
        continue

    fner.write(" ".join([each[0] + "/" + each[1] for each in nlp.ner(line) if len(each) == 2]) + "\n")
    ftag.write(" ".join([each[0] + "/" + each[1] for each in nlp.pos_tag(line) if len(each) == 2]) + "\n")
fner.close()
ftag.close()
