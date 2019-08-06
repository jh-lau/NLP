"""
  User: Liujianhan
  Time: 1:50
 """
__author__ = 'liujianhan'

import os
import re
from hanziconv import HanziConv
import jieba

if __name__ == '__main__':
    count = 0
    target_path = 'D:\\Github\\NLP\\Artificial_Intelligence_for_NLP\\Week_04_0727\\data\\text'
    os.chdir(target_path)
    for x in os.listdir(os.curdir):
        if os.path.isdir(x):
            target_ = os.path.abspath(x)
            for file in os.listdir(target_):
                file_path = os.path.join(target_, file)
                file_name, ext = os.path.splitext(file_path)
                if not ext:
                    with open(file_name, 'r', encoding='utf-8') as f1:
                        count += 1
                        percentage = (count / 1298)*100
                        print(f"{percentage: .2f} %")
                        with open('wiki_cut_' + str(count), 'w', encoding='utf-8') as f2:
                            for each_line in f1:
                                if each_line.strip():
                                    temp_result = []
                                    to_simplified = HanziConv.toSimplified(each_line)
                                    get_char = re.findall('[\u4e00-\u9fa5]+', to_simplified)
                                    for each in get_char:
                                        temp_result += list(jieba.cut(each))

                                    f2.write(' '.join(temp_result) + '\n')
