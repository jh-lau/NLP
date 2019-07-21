"""
  User: Liujianhan
  Time: 12:50
 """
__author__ = 'liujianhan'

from functools import lru_cache

solution_ = {}


@lru_cache(maxsize=2 ** 10)
def edit_distance(string1, string2):
    if string1 and string2:

        tail_s1 = string1[-1]
        tail_s2 = string2[-1]

        candidates = [
            (edit_distance(string1[:-1], string2) + 1, 'DEL {}'.format(tail_s1)),
            (edit_distance(string1, string2[:-1]) + 1, 'ADD {}'.format(tail_s2)),
        ]

        if tail_s1 == tail_s2:
            both_forward = (edit_distance(string1[:-1], string2[:-1]) + 0, '')
        else:
            both_forward = (edit_distance(string1[:-1], string2[:-1]) + 1, 'SUB {} => {}'.format(tail_s1, tail_s2))

        candidates.append(both_forward)

        min_distance, operation = min(candidates, key=lambda x: x[0])

        solution_[(string1, string2)] = operation

        return min_distance

    return len(string1) if string1 else len(string2)


if __name__ == '__main__':
    edit_distance('aebd', 'abcd')
