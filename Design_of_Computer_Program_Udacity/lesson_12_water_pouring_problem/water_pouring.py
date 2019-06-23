"""
  User: Liujianhan
  Time: 16:39
 """
__author__ = 'liujianhan'


def pour_problem(X, Y, goal, start=(0, 0)):
    """X and Y are the capacity of glasses; (x, y) is current fill levels
    and represents a state. The goal is a level that can be in either glass.
    Start at start state and follow successors until we reach the goal.
    Keep track of frontier and previously explored; fail when no frontier."""
    if goal in start:
        return [start]
    explored = set()  # set of states we have visited
    frontier = [[start]]  # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        (x, y) = path[-1]  # Last state in the first path of the frontier
        for (state, action) in successors(x, y, X, Y).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if goal in state:
                    return path2
                else:
                    frontier.append(path2)
    return Fail


Fail = []
