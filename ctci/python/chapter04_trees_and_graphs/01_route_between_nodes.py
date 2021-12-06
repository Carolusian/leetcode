# 4.1 Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
# route between two nodes.

# Keywords: BFS, DFS

# Solution: a typical BFS or DFS problem. See also 2059_minimum_options_to_convert_number.py in weekly-contest-265

# Hints:#127

import unittest
import collections
from typing import List, Dict, Set, Deque


def is_route_dfs(
    graph: Dict[str, List[str]], start: str, end: str, seens: Set[str]
) -> bool:
    res = []
    for v in graph[start]:
        if v == end: # or is_route_recursive() .. this may be better
            return True

        if v not in seens:
            seens.add(v)
            res.append(is_route_dfs(graph, v, end, seens))
    return any(res)


def is_route_bfs(graph: Dict[str, List[str]], start: str, end: str) -> bool:
    queue: Deque[str] = collections.deque()
    seen: Set[str] = set()
    queue.append(start)

    while queue:
        val = queue.popleft()
        if val == end:
            return True

        if val not in seen:
            seen.add(val)
            for v in graph[val]:
                queue.append(v)
    return False


graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D", "E"],
    "D": ["B", "C"],
    "E": ["C", "F"],
    "F": ["E", "O", "I", "G"],
    "G": ["F", "H"],
    "H": ["G"],
    "I": ["F", "J"],
    "O": ["F"],
    "J": ["K", "L", "I"],
    "K": ["J"],
    "L": ["J"],
    "P": ["Q", "R"],
    "Q": ["P", "R"],
    "R": ["P", "Q"],
}

tests = [
    ("A", "L", True),
    ("A", "B", True),
    ("H", "K", True),
    ("L", "D", True),
    ("P", "Q", True),
    ("Q", "P", True),
    ("Q", "G", False),
    ("R", "A", False),
    ("P", "B", False),
]


class Test(unittest.TestCase):
    def test_is_route(self):
        for tc in tests:
            start, end, expect = tc
            print(start, end, expect)
            self.assertEqual(is_route_dfs(graph, start, end, set()), expect)
            self.assertEqual(is_route_bfs(graph, start, end), expect)


if __name__ == "__main__":
    unittest.main()
