"""
  User: Liujianhan
  Time: 21:55
 """
__author__ = 'liujianhan'
import doctest


def bridge_successors(state):
    """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the 'light', and t is a number indicating the elapsed time. Action is represented
    as a tuple (person1, person2, arrow), where arrow is '->' for here to there and
    '<-' for there to here.
    e.g: action (2, 2, '->') means that the person with a travel time of 2
    crossed from here to there alone."""
    here, there, t = state
    if 'light' in here:
        return dict(((here - frozenset([a, b, 'light']),
                      there | frozenset([a, b, 'light']),
                      t + max(a, b)),
                     (a, b, '->'))
                    for a in here if a is not 'light'
                    for b in here if b is not 'light')
    else:
        return dict(((here | frozenset([a, b, 'light']),
                      there - frozenset([a, b, 'light']),
                      t + max(a, b)),
                     (a, b, '<-'))
                    for a in there if a is not 'light'
                    for b in there if b is not 'light')


def bridge_successors_2(state):
    """Return a dict of {state:action} pairs. A state is a
    (here, there) tuple, where here and there are frozensets
    of people (indicated by their travel times) and/or the light."""
    here, there = state
    if 'light' in here:
        return dict(((here - frozenset([a, b, 'light']),
                      there | frozenset([a, b, 'light'])),
                     (a, b, '->'))
                    for a in here if a is not 'light'
                    for b in here if b is not 'light')
    else:
        return dict(((here | frozenset([a, b, 'light']),
                      there - frozenset([a, b, 'light'])),
                     (a, b, '<-'))
                    for a in there if a is not 'light'
                    for b in there if b is not 'light')


def bridge_problem(here):
    here = frozenset(here) | frozenset(['light'])
    explored = set()  # set of states we have visited
    # State will be a (people-here, people-there, time-elapsed)
    frontier = [[(here, frozenset(), 0)]]  # ordered list of paths we have blazed
    if not here:
        return frontier[0]

    while frontier:
        path = frontier.pop(0)

        for (state, action) in bridge_successors(path[-1]).items():
            if state not in explored:
                here, there, t = state
                explored.add(state)
                path2 = path + [action, state]
                if not here:  # That is, nobody left here
                    return path2
                else:
                    frontier.append(path2)
                    frontier.sort(key=elapsed_time)
    return []


def bridge_problem_2(here):
    """Tests for the goal later, after pulling a state off the frontier, not when we're about to put it on the
    frontier."""
    here = frozenset(here) | frozenset(['light'])
    explored = set()
    frontier = [[(here, frozenset(), 0)]]
    if not here:
        return frontier[0]

    while frontier:
        path = frontier.pop(0)

        here_1, there_1, t1 = state_1 = path[-1]
        if not here_1 or here_1 == {'light'}:  # Check for solution when we pull best path
            return path

        for (state, action) in bridge_successors(path[-1]).items():
            if state not in explored:
                here, there, t = state
                explored.add(state)
                path2 = path + [action, state]
                # Don't check for solution when extend a path
                frontier.append(path2)
                frontier.sort(key=elapsed_time)
    return []


def elapsed_time(path):
    return path[-1][2]


def path_states(path):
    """Return a list of states in this path."""
    return path[0::2]


def path_actions(path):
    """Return a list of actions in this path."""
    return path[1::2]


def path_test():
    test_path = [(frozenset([1, 10]), frozenset(['light', 2, 5]), 5),  # state 1
                 (5, 2, '->'),  # action 1
                 (frozenset([10, 5]), frozenset([1, 2, 'light']), 2),  # state 2
                 (2, 1, '->'),  # action 2
                 (frozenset([1, 2, 10]), frozenset(['light', 5]), 5),
                 (5, 5, '->'),
                 (frozenset([1, 2]), frozenset(['light', 10, 5]), 10),
                 (5, 10, '->'),
                 (frozenset([1, 10, 5]), frozenset(['light', 2]), 2),
                 (2, 2, '->'),
                 (frozenset([2, 5]), frozenset([1, 10, 'light']), 10),
                 (10, 1, '->'),
                 (frozenset([1, 2, 5]), frozenset(['light', 10]), 10),
                 (10, 10, '->'),
                 (frozenset([1, 5]), frozenset(['light', 2, 10]), 10),
                 (10, 2, '->'),
                 (frozenset([2, 10]), frozenset([1, 5, 'light']), 5),
                 (5, 1, '->'),
                 (frozenset([2, 10, 5]), frozenset([1, 'light']), 1),
                 (1, 1, '->')]
    assert path_states(test_path) == [(frozenset([1, 10]), frozenset(['light', 2, 5]), 5),  # state 1
                                      (frozenset([10, 5]), frozenset([1, 2, 'light']), 2),  # state 2
                                      (frozenset([1, 2, 10]), frozenset(['light', 5]), 5),
                                      (frozenset([1, 2]), frozenset(['light', 10, 5]), 10),
                                      (frozenset([1, 10, 5]), frozenset(['light', 2]), 2),
                                      (frozenset([2, 5]), frozenset([1, 10, 'light']), 10),
                                      (frozenset([1, 2, 5]), frozenset(['light', 10]), 10),
                                      (frozenset([1, 5]), frozenset(['light', 2, 10]), 10),
                                      (frozenset([2, 10]), frozenset([1, 5, 'light']), 5),
                                      (frozenset([2, 10, 5]), frozenset([1, 'light']), 1)]
    assert path_actions(test_path) == [(5, 2, '->'),  # action 1
                                       (2, 1, '->'),  # action 2
                                       (5, 5, '->'),
                                       (5, 10, '->'),
                                       (2, 2, '->'),
                                       (10, 1, '->'),
                                       (10, 10, '->'),
                                       (10, 2, '->'),
                                       (5, 1, '->'),
                                       (1, 1, '->')]
    return 'tests pass'


def test():
    assert bridge_successors((frozenset([1, 'light']), frozenset([]), 3)) == {
        (frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}

    assert bridge_successors((frozenset([]), frozenset([2, 'light']), 0)) == {
        (frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}

    here1 = frozenset([1, 'light'])
    there1 = frozenset([])

    here2 = frozenset([1, 2, 'light'])
    there2 = frozenset([3])

    assert bridge_successors_2((here1, there1)) == {
        (frozenset([]), frozenset([1, 'light'])): (1, 1, '->')}

    assert bridge_successors_2((here2, there2)) == {
        (frozenset([1]), frozenset(['light', 2, 3])): (2, 2, '->'),
        (frozenset([2]), frozenset([1, 3, 'light'])): (1, 1, '->'),
        (frozenset([]), frozenset([1, 2, 3, 'light'])): (2, 1, '->')}

    return 'tests pass'


class TestBridge: """
>>> elapsed_time((bridge_problem([1, 2, 5, 10])))
17

>>> [elapsed_time(bridge_problem([1, 2, 4, 8, 16][:n])) for n in range(6)]
[0, 1, 2, 7, 15, 28]

>>> [elapsed_time(bridge_problem([1,1,2,3,5,8,13,21][:n])) for n in range(8)]
[0, 1, 1, 2, 6, 12, 19, 30]

>>> S1 = [(2, 1, '->'), (1, 1, '<-'), (5, 10, '->'), (2, 2, '<-'), (2, 1, '->')]
>>> S2 = [(2, 1, '->'), (2, 2, '<-'), (5, 10, '->'), (1, 1, '<-'), (2, 1, '->')]
>>> path_actions(bridge_problem([1,2,5,10])) in (S1, S2)
True

>>> path_actions(bridge_problem([1,2,5,10,15,20]))
[(2, 1, '->'), (1, 1, '<-'), (10, 5, '->'), (2, 2, '<-'), (2, 1, '->'), (1, 1, '<-'), (15, 20, '->'), (2, 2, '<-'), (2, 1, '->')]

>>> path_actions(bridge_problem([1,2,4,8,16,32]))
[(2, 1, '->'), (1, 1, '<-'), (8, 4, '->'), (2, 2, '<-'), (2, 1, '->'), (1, 1, '<-'), (16, 32, '->'), (2, 2, '<-'), (2, 1, '->')]
"""


if __name__ == '__main__':
    print(test())
    # print(path_test())
    # print(bridge_problem([1, 2, 5, 10]))
    # print(bridge_problem([1, 2, 5, 10])[1::2])
    # print(doctest.testmod())
