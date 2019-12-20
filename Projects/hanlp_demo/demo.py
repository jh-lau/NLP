"""
  User: Liujianhan
 """
__author__ = 'liujianhan'

from pyhanlp import *

corpus = "你好,欢迎在python中调用HanLP的API."

if __name__ == '__main__':
    print(HanLP.segment(corpus))
