"""
  User: Liujianhan
  Time: 23:36
 """
__author__ = 'liujianhan'


def get_synonyms(model, target, length=200):
    candidates = []

    def helper(model, target):
        nonlocal candidates
        result = [x[0] for y in target for x in model.wv.most_similar(y)]
        candidates += result
        return helper(model, result) if len(candidates) < length else candidates

    return set(helper(model, target))
