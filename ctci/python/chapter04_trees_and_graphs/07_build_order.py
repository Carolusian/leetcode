# 4.7 Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
# projects, where the second project is dependent on the first project). All of a project's dependencies
# must be built before the project is. Find a build order that will allow the projects to be built. If there
# is no valid build order, return an error.
# EXAMPLE
# Input:
# projects: a, b, c, d, e, f
# dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
# Output: f, e, a, b, d, c
# Hints: #26, #47, #60, #85, #725, #133
#
# Keywords: adjacency list, graph, pop and re-append a queue
#
# Solution 1: this method causes TLE on leetcode
# - if a project has dependency, move back to the end of the queue
# - maintain and dependency graph and a queue of projects to be built
# - pop the queue, check circular dependency
# - if the item has dependency, append back to queue
# - otherwise, append to return list
#
# Solution 2: DFS, topological sort, Kahn's algorithm
#
# See: https://leetcode.com/problems/course-schedule-ii/

import collections
import unittest

from typing import List


def build_order(nums: List[str], dependencies: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)

    """
    'd': ['a', 'b'], 
    'b': ['f'], 
    'a': ['f'], 
    'c': ['d']
    """
    graph = collections.defaultdict(list)
    for dep in dependencies:
        prereq, dependent = dep
        graph[dependent].append(prereq)

    # check if circular dependencies, return empty if no valid build order
    # actually, this checking can be done during the loop of the order building process

    # return a build order starting with projects
    ret = []
    q = collections.deque(nums)
    while q:
        proj = q.popleft()
        deps = [d for d in graph[proj] if d not in ret]

        # check circular dependencies
        for d in deps:
            if proj in graph[d]:
                return []

        if not deps:
            ret.append(proj)
        else:
            q.append(proj)

    return ret

# TODO: solve with topological sort


class Test(unittest.TestCase):
    def test_build_order(self):
        nums = ["a", "b", "c", "d", "e", "f"]
        dependencies = [["a", "d"], ["f", "b"], ["b", "d"], ["f", "a"], ["d", "c"]]
        self.assertEqual(len(build_order(nums, dependencies)), len(nums))

        # circular
        nums = ["a", "b", "c", "d", "e", "f"]
        dependencies = [
            ["a", "d"],
            ["f", "b"],
            ["b", "d"],
            ["f", "a"],
            ["d", "c"],
            ["d", "a"],
        ]
        self.assertEqual(build_order(nums, dependencies), [])


if __name__ == "__main__":
    unittest.main()
