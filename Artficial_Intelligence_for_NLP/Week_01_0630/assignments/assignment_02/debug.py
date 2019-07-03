"""
  User: Liujianhan
  Time: 16:59
 """
import random
from collections import defaultdict
from Week_01_0630.assignments.assignment_02.rule_responses import rule_responses
from Week_01_0630.assignments.assignment_02.chinese_cut_single import cut_single
import jieba

__author__ = 'liujianhan'


def is_variable(pat):
    return pat.startswith('?') and all(s.isalpha() for s in pat[1:])


def is_pattern_segment(pattern):
    return pattern.startswith('?*') and all(s.isalpha() for s in pattern[2:])


def pat_match(pattern, saying):
    """Return the list of [('?x', 'something'),....]"""
    if not pattern or not saying:
        return []
    if is_variable(pattern[0]):
        return [(pattern[0], saying[0])] + pat_match(pattern[1:], saying[1:])
    else:
        if pattern[0] != saying[0]:
            return []
        else:
            return pat_match(pattern[1:], saying[1:])


fail = [True, None]


def is_match(rest, saying):
    if not rest and not saying:
        # rest == saying
        return True
    if not all(a.isalpha() for a in rest[0]):
        # reach another ?* and out
        return True
    if rest[0] != saying[0]:
        return False
    return is_match(rest[1:], saying[1:])


def segment_match(pattern, saying):
    """Match as long as pattern goes."""
    seg_pat, rest = pattern[0], pattern[1:]
    seg_pat = seg_pat.replace('?*', '?')
    if not rest:
        return (seg_pat, saying), len(saying)
    for i, token in enumerate(saying):
        # Modify condition like pat_match_with_seg('?*X hello'.split(), 'hi hello you'.split()) raise an index error.
        try:
            if rest[0] == token and is_match(rest[1:], saying[(i + 1):]):
                return (seg_pat, saying[:i]), i
        except IndexError:
            return (seg_pat, saying[:i]), i
    return (seg_pat, saying), len(saying)


def pat_match_with_seg(pattern, saying):
    if not pattern or not saying:
        return []
    pat = pattern[0]

    if is_variable(pat):
        return [(pat, saying[0])] + pat_match_with_seg(pattern[1:], saying[1:])
    elif is_pattern_segment(pat):
        match, index = segment_match(pattern, saying)
        return [match] + pat_match_with_seg(pattern[1:], saying[index:])
    elif pat == saying[0]:
        return pat_match_with_seg(pattern[1:], saying[1:])
    else:
        return fail


def pat_to_dict(patterns):
    """Get a dict to store key:value of variable:target"""
    return {k: ' '.join(v) if isinstance(v, list) else v for k, v in patterns}


def substitute(rule, parsed_rules):
    """Substitute the variable in rule with dict value in parsed_rules"""
    if not rule:
        return []
    return [parsed_rules.get(rule[0], rule[0])] + substitute(rule[1:], parsed_rules)


defined_patterns = {
    "I need ?X": ["Image you will get ?X soon", "Why do you need ?X ?"],
    "My ?X told me something": ["Talk about more about your ?X", "How do you think about your ?X ?"]
}


def get_response(saying, rules=defined_patterns):
    # need to obey the rule in defined_patterns's key
    result = []
    for k, v in rules.items():
        t = pat_match(k.split(), saying.split())
        if t:
            result = t, v
    if result:
        dictionary = pat_to_dict(result[0])
        answer = random.choice(result[1])
        return ' '.join(substitute(answer.split(), dictionary))
    return 'Match failed, more instance of rules are needed.'


def get_response_star(saying, response_rules=rule_responses):
    result = []
    for question, answer in response_rules.items():
        temp = pat_match_with_seg(question.split(), saying.split())
        if len(temp) > 1 and None not in temp:
            result = substitute(random.choice(answer).split(), pat_to_dict(temp))
    if not result:
        return random.choice(response_rules['?*x'])
    return ' '.join(result)


def new_split(string):
    result = []
    temp = list(jieba.cut(string))
    for i, each in enumerate(temp):
        if each == '?':
            if len(temp) == i + 1:
                result.append(each)
            elif temp[i + 1] == '*':
                result.append(temp[i] + temp[i + 1] + temp[i + 2])
            elif temp[i + 1].isalpha():
                result.append(temp[i] + temp[i + 1])
        elif len(each) == 1 and (each == '*' or each.isupper() or each.islower()):
            continue
        elif each != ' ':
            result.append(each)
    return result


test_rules = {
    '?*x好的?*y': ['好的', '你是一个很正能量的人'],
    # '?*x就像?*y': ['你觉得?x和?y有什么相似性？', '?x和?y真的有关系吗？', '怎么说？']
}


def get_response_star_new(saying, response_rules=rule_responses):
    result = []
    last = []
    for question, answer in response_rules.items():

        temp = pat_match_with_seg(new_split(question), new_split(saying))
        # pop the ('?x", '') tuple in the pattern match list.
        for k, v in temp:
            if not v:
                temp.pop(temp.index((k, v)))
        if len(temp) > 1 and None not in temp:
            result = substitute(new_split(random.choice(answer)), pat_to_dict(temp))

    if not result:
        return random.choice(response_rules['?*x'])

    for each in result:
        last.append(''.join(each.split()))
    return ''.join(last)


if __name__ == '__main__':
    # print(segment_match('?*P is very good'.split(), 'My dog and my cat is very good'.split()))
    # print(pat_match_with_seg('?*X hello ?*Y'.split(), 'wold hello yes'.split()))
    # print(pat_match_with_seg('what'.split(), 'I am Mike, fa '.split()))
    # print(substitute("I was ?X".split(),
    #                  pat_to_dict(pat_match_with_seg('I need ?*X'.split(),
    #                                                 "I need an iPhone".split()))))
    # print(get_response_star('world hello yes'))
    # print(get_response_star_new('你一直这么干'))
    print(get_response_star_new('我妈妈对我很好'))
    # print(get_response_star_new('我讨厌他'))
    # print(get_response_star_new('曾经我记得这个人'))
    # print(new_split('你觉得我是帅哥吗'))
    # print(pat_match_with_seg(new_split('你觉得?*y有什么意义呢?'), new_split('你觉得睡觉有什么意义呢?')))
    # print(new_split('你觉得?*y有什么意义呢?'))
    # print(new_split('你觉得睡觉有什么意义呢?'))
