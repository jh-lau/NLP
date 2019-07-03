"""
  User: Liujianhan
  Time: 16:16
 """
__author__ = 'liujianhan'
import re


def cut_single(split_list):
    result = []
    for i, each in enumerate(split_list):
        if each.isalpha() and not(each.islower() or each.isupper()):
            continue
        result.append(each)
    regular = re.findall('[a-zA-Z]+', split_list)
    result += regular
    return result


if __name__ == '__main__':
    print(cut_single('我是中国人，我爱China北京天安门hifa好厉害f我们.'))
