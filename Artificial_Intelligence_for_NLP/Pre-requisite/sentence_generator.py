"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/6/7
  Time: 23:39
 """
import random

__author__ = 'liujianhan'


class Solution:
    def __init__(self):
        self.article = ['一个', '这个']
        self.noun = ['女人', '篮球', '桌子', '小猫']
        self.verb = ['看着', '听着', '看见']
        self.adj = ['蓝色的', '好看的', '小小的', '年轻的']

    def noun_phrase(self):
        return ''.join([random.choice(self.article),
                       random.choice(self.adj),
                       random.choice(self.noun)])

    def verb_phrase(self):
        return ''.join([random.choice(self.verb),
                        random.choice(self.article),
                        random.choice(self.noun)])

    def generate(self):
        return ''.join([self.noun_phrase(), self.verb_phrase()])


if __name__ == '__main__':
    test = Solution()
    for i in range(20):
        print(test.generate())

