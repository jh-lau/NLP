"""
  User: Liujianhan
 """

from pyhanlp import *

corpus = "你好,欢迎在python中调用HanLP的API"

if __name__ == '__main__':
    segment = DoubleArrayTrieSegment()
    segment.enablePartOfSpeechTagging(True)
    HanLP.Config.ShowTermNature = True
    print(segment.seg('上海市虹口区大连西路550号SISU'))
