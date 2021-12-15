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


# solve with topological sort
# method 1: DFS + stack: https://www.geeksforgeeks.org/topological-sorting/
# See also: 07_Topological-Sorting.png
"""core implementation

if v in graphp[vertex]:
    topo_sort(v, graph)
if not seen[vertex]:
    stack.append(vertex)
    seen[vertex] = True
"""


def build_order_topologic_sort(
    nums: List[str], dependencies: List[List[str]]
) -> List[str]:
    # seen has 3 states: 0, 1, 2
    # 1 represent inprogress
    # 3 states can be used to check circularity
    graph, seen = collections.defaultdict(list), collections.defaultdict(int)
    stack, n = [], len(nums)

    # build graph
    """
    'a': ['d'], 
    'f': ['b', 'a'], 
    'b': ['d'], 
    'd': ['c']
    """
    for dep in dependencies:
        prereq, dependent = dep
        graph[prereq].append(dependent)

    """recursive function for topological sort
    :return: if continue or not, do not continue is cirularity is detected
    """

    def topo_sort(vertex: str, graph) -> bool:
        # check circular
        if seen[vertex] == 1:
            return False

        if not seen[vertex]:        # only change 0: not visited to 1: inprogress
            seen[vertex] = 1

        # recursive implementation on topo_sort
        for v in graph[vertex]:
            if not topo_sort(v, graph):
                return False

        if seen[vertex] != 2:
            stack.append(vertex)
            seen[vertex] = 2
        return True

    for vertex in nums:
        if not topo_sort(vertex, graph):
            return []

    return stack[::-1]


# method 2: kahn: https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/


class Test(unittest.TestCase):
    def test_build_order(self):
        nums = ["a", "b", "c", "d", "e", "f"]
        dependencies = [["a", "d"], ["f", "b"], ["b", "d"], ["f", "a"], ["d", "c"]]
        self.assertEqual(len(build_order(nums, dependencies)), len(nums))
        self.assertEqual(len(build_order_topologic_sort(nums, dependencies)), len(nums))

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
        self.assertEqual(build_order_topologic_sort(nums, dependencies), [])


if __name__ == "__main__":
    unittest.main()
