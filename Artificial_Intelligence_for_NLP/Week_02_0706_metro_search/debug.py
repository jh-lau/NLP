"""
  User: Liujianhan
  Time: 17:41
 """
from collections import defaultdict

__author__ = 'liujianhan'

number_graph_2 = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6, 7],
    4: [2, 8, 9],
    5: [2, 10, 11],
    6: [3, 12, 13],
    7: [3, 14, 15],
    8: [4],
    9: [4],
    10: [5],
    11: [5],
    12: [6],
    13: [6],
    14: [7],
    15: [7]
}

simple = {
    '北京': ['太原', '沈阳'],
    '太原': ['北京', '西安', '郑州'],
    '兰州': ['西安'],
    '郑州': ['太原'],
    '西安': ['兰州', '长沙'],
    '长沙': ['福州', '南宁'],
    '沈阳': ['北京'],
    '福州': ['长沙'],
    '南宁': ['长沙'],
}

simple_connection_info_src = {
    '北京': ['太原', '沈阳'],
    '太原': ['北京', '西安', '郑州'],
    '兰州': ['西安'],
    '郑州': ['太原'],
    '西安': ['兰州', '长沙'],
    '长沙': ['福州', '南宁'],
    '沈阳': ['北京']
}
simple_connection_info = defaultdict(list)
simple_connection_info.update(simple_connection_info_src)


def bfs(graph, start):
    visited, seen = [start], set()
    while visited:
        frontier = visited.pop()
        if frontier in seen: continue
        for successor in graph[frontier]:
            if successor in seen: continue
            print(successor)
            visited = [successor] + visited
        seen.add(frontier)
    return seen


class DFS:
    seen = set()

    def search(self, graph, start):
        self.seen.add(start)
        print(start)
        if len(graph[start]) == 1:
            return
        for successor in graph[start]:
            if successor in self.seen:
                continue
            self.search(graph, successor)
        return self.seen


# print(DFS().search(number_graph_2, 1))
# print(DFS().search(simple, '北京'))

# print(DFS().search(simple_connection_info, '太原'))
print(DFS().search(simple_connection_info, '北京'))
# print(simple_connection_info['南宁'])
# print(simple_connection_info)
print(bfs(simple_connection_info, '北京'))
