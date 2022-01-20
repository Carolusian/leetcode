# 4.12 Paths with Sum: You are given a binary tree in which each node contains an integer value (which
# might be positive or negative). Design an algorithm to count the number of paths that sum to a
# given value. The path does not need to start or end at the root or a leaf, but it must go downwards
# (traveling only from parent nodes to child nodes).
# Hints:#6, #14, #52, #68, #77, #87, #94, #103, #108, #115

# Keywords: DFS, divide and conquer, brutal force, running sum
# Solution 1:
# - brutal force, find all paths using DFS, then sum subpaths
# - Time: O(N logN) - O(N**2);

# Solution 2:
# - every node has a only one path to reach it, reach it has one running sum
# - save the running sum to a hashtable
# - then, runingsum_y - target_sum = runningsum_x.
# - that means, the count sum to the target_sum can be queried from hashtable storing
# - the count of runningsum_x
# - Time: O(logN) - O(N), Space: O(1) - O(N)

# Core code: take a linked list as example

"""
    running_y = running_y + node.val
    hashtable[running_y] += 1
    running_x = running_y - target_sum
    cnt = hashtable[running_x]
    l_cnt = fn(node.next, target_sum, running_y, hashtable) 
"""

# See: https://leetcode-cn.com/problems/path-sum-ii/solution/yi-pian-wen-zhang-jie-jue-suo-you-er-cha-oo63/

import unittest
import collections
from typing import List, Optional
from binary_tree import Tree, TreeNode


def paths_with_sum(root: Optional[TreeNode], target_sum: int) -> int:
    """Solution 1: Brutal Force, DFS to find all paths"""
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


def paths_with_sum2(root: Optional[TreeNode], target_sum: int) -> int:
    """Solution 2: save intermediary running sum into hash table, similar to DP algorithm"""
    d = collections.defaultdict(int)
    
    def increment(hashtable, k, delta):
        hashtable[k] += delta
        if hashtable[k] < 0:
            hashtable[k] = 0

    def fn(
        node: Optional[TreeNode],
        target_sum: int,
        running_y: int,
        hashtable: collections.defaultdict,
    ):
        if not node: return 0
        running_y = running_y + node.val
        running_x = running_y - target_sum

        cnt = hashtable[running_x]
        if running_y == target_sum:
            cnt += 1
        
        increment(hashtable, running_y, 1)
        l_cnt = fn(node.left, target_sum, running_y, hashtable) 
        r_cnt = fn(node.right, target_sum, running_y, hashtable)
        # the reason we minus 1 for key running_y is because once the left and right
        # children of the node are recursively travesed, it will back out to the parent node
        # we dont want the this running_y to be used as running_x in another branch
        # of the parent node
        # minus 1 is not necessary if we just have a linked list rather than a binary tree
        increment(hashtable, running_y, -1)
        return cnt + l_cnt + r_cnt


    return fn(root, target_sum, 0, d)


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
    # tree = Tree.from_list(test_cases[0][0])
    # root = tree.root
    # print(paths_with_sum2(root, 8))
