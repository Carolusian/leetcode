# 4.1 Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
# route between two nodes.

# Keywords: BFS, DFS

# Solution: a typical BFS or DFS problem. See also 2059_minimum_options_to_convert_number.py in weekly-contest-265

# Hints:#127

import unittest
from typing import List, Dict


def is_route_recursive(
    graph: Dict[str, List[str]], start: str, end: str, seens: List[str]
) -> bool:
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
        pass


if __name__ == "__main__":
    pass
