# 4.9 BST Sequences: A binary search tree was created by traversing through an array from left to right
# and inserting each element. Given a binary search tree with distinct elements, print all possible
# arrays that could have led to this tree.
# EXAMPLE
# Input:
# Output: {2, 1, 3}, {2, 3, 1}
# Hints: #39, #48, #66, #82
#
# Keywords: divide and conquer, weaving two arrays and keep relative order
#
# Solution:
# - the root element is always the first elem in the array

# See:
# - https://mohit.athwani.net/blog/weaving-two-arrays
# - https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/

"""
fn(3) -> 3 (fn(1), fn(4)) or 3 (fn(4), fn(1))
3 ((1, fn(2)), (4, fn(5))) or 3 (4, fn(5), 1, fn(2))
3 (1, 2)(4, 5) or 3(4,5)(1,2)
"""

import unittest
from typing import List
from binary_tree import Tree, TreeNode


tree_vals = [3, 1, 4, 2, 5]


def bst_sequences(nums: List[int]):
    tree = Tree.create_bst(tree_vals)
    root = tree.root

    def fn(node):
        if node:
            print(node.val)

        if node.left:
            fn(node.left)
        if node.right:
            fn(node.right)

    fn(root)


class Test(unittest.TestCase):
    pass


"""
e.g. 
3 [1 2]
3 [4 5]

=== sample steps ===
w([1,2], [4,5], [3], []) ->
w([2], [4, 5], [3,1], []) | w([1, 2], [5], [3, 4], []) ->
[3,1,2,4,5], [3,1,4,2,5], [3,1,4,5,2], [3,1,2,4,5] | ...

The above binary routes recusion approach(just divide and conquer with two scenarios): 
- swap the orders of the numbers between the two array
- but still, keeps the respect order of the numbers within the same array
"""


def weave(p: List[int], q: List[int], prefix: List[int], res: List[List[int]]):
    """weave two list of the same prefix, return None as result is saved in res"""
    if len(p) == 0 or len(q) == 0:
        result = prefix.copy()
        result.extend(p)
        result.extend(q)
        res.append(result)
        return
    
    # scenario 1
    prefix.append(p[0])
    weave(p[1:], q, prefix, res)
    prefix.pop()

    # scenario 2
    prefix.append(q[0])
    weave(p, q[1:], prefix, res)
    prefix.pop()
    return res


if __name__ == "__main__":
    # print(bst_sequences(tree_vals))
    # weave([], [1])
    # weave([1], [])
    res = []
    weave([1, 2], [4, 5], [3], res)
    print(res)
