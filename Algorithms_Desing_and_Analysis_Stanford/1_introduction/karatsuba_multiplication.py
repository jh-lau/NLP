"""
  User: Liujianhan
  Time: 23:00
 """
__author__ = 'liujianhan'


def karatsuba_multiplication(num_1, num_2):
    if num_1 < 10 or num_2 < 10:
        return num_1 * num_2
    num_1 = str(num_1)
    num_2 = str(num_2)

    max_length = max(len(num_1), len(num_2))
    split_position = max_length >> 1
    high_1, low_1 = int(num_1[:-split_position]), int(num_1[-split_position:])
    high_2, low_2 = int(num_2[:-split_position]), int(num_2[-split_position:])
    t0 = karatsuba_multiplication(low_1, low_2)
    t1 = karatsuba_multiplication((low_1 + high_1), (low_2 + high_2))
    t2 = karatsuba_multiplication(high_1, high_2)

    return (t2 * 10 ** (2 * split_position)) + ((t1 - t2 - t0) * 10 ** split_position) + t0


def test():
    assert karatsuba_multiplication(5678, 1234) == 5678 * 1234
    return 'test pass'


if __name__ == '__main__':
    print(test())
