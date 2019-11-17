"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/6/7
  Time: 23:21
 """
__author__ = 'liujianhan'
from data_structure.function_process_time import RuntimeTest


class Solution:
    @staticmethod
    @RuntimeTest()
    def get_factors(num):
        result = []
        while num % 2 == 0:
            result.append(2)
            num = num / 2

        while num % 3 == 0:
            result.append(3)
            num = num / 3

        while num % 5 == 0:
            result.append(5)
            num = num / 5

        return tuple(result) if num == 1 and result else None

    @staticmethod
    def get_simple_factors(n):
        simple_words = [2, 3, 5]

        if n in simple_words:
            return [n]

        for s in simple_words:
            could_be_divided, remain = (n % s == 0), n / s

            if could_be_divided and Solution.get_simple_factors(remain):
                return [s] + Solution.get_simple_factors(remain)

        return None


if __name__ == '__main__':
    test_1 = 1845281250
    test_2 = 3690562500
    test_3 = 1230187500
    test_4 = 10023750

    # Solution.get_factors(test_1)
    # Solution.get_factors(test_2)
    # Solution.get_factors(test_3)
    # Solution.get_factors(test_4)
    # Solution.get_factors(6)

    print(Solution.get_simple_factors(test_1))
    print(Solution.get_simple_factors(test_2))
    print(Solution.get_simple_factors(test_3))
    print(Solution.get_simple_factors(test_4))
