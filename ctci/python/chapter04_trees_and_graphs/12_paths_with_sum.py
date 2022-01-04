# 4.12 Paths with Sum: You are given a binary tree in which each node contains an integer value (which
# might be positive or negative). Design an algorithm to count the number of paths that sum to a
# given value. The path does not need to start or end at the root or a leaf, but it must go downwards
# (traveling only from parent nodes to child nodes).
# Hints:#6, #14, #52, #68, #77, #87, #94, #103, #108, #115

# Keywords: DFS, divide and conquer, brutal force
# Solution 1: 
# - brutal force, find all paths using DFS, then sum subpaths
# - Time: O(N logN) - O(N**2); 

# Solution 2: TODO
# - Time: O(logN) - O(N), Space: O(1) - O(N)

import unittest
from typing import List, Optional
from binary_tree import Tree, TreeNode


def paths_with_sum(root: Optional[TreeNode], target_sum: int) -> int:
    cnt = 0
    paths = []

    def fn(node: Optional[TreeNode], prev: List[int]):
        if not node:
            return

        paths.append(prev + [node.val])
        if node.left:
            fn(node.left, prev + [node.val])
        if node.right:
            fn(node.right, prev + [node.val])

    fn(root, [])

    for path in paths:
        for i in range(len(path)):
            if sum(path[i:]) == target_sum:
                cnt += 1
    return cnt


"""
tree 1:
        10
       5      -3
     3     2    11
 3  -2   1

tree 2:
           5
       4       8
    11    13     4
 7   2   5   1
"""

test_cases = (
    ([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8, 3),
    ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22, 3),
)


class Test(unittest.TestCase):
    def test_paths_with_sum(self):
        for tc in test_cases:
            tree_nodes, target, expect = tc
            tree = Tree.from_list(tree_nodes)
            self.assertEqual(paths_with_sum(tree.root, target), expect)


if __name__ == "__main__":
    unittest.main()
