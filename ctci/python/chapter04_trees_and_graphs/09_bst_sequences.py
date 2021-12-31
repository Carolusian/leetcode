# 4.9 BST Sequences: A binary search tree was created by traversing through an array from left to right
# and inserting each element. Given a binary search tree with distinct elements, print all possible
# arrays that could have led to this tree.
# EXAMPLE
# Input:
# Output: {2, 1, 3}, {2, 3, 1}
# Hints: #39, #48, #66, #82
#
# Keywords: divide and conquer, weaving two arrays and keep relative order, weave, backtracking

# Solution 1:
# - the root element is always the first elem in the array
# - weave function: left, right, prefix, res

# Solution 2:
# - backtracking, put parent to weave array, and left and right to next choices

# See:
# - https://mohit.athwani.net/blog/weaving-two-arrays
# - https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/
r"""Tree for testing
     3
    / \
   1   4
    \   \
     2   5
"""

"""
fn(3) -> 3 (fn(1), fn(4)) or 3 (fn(4), fn(1))
3 ((1, fn(2)), (4, fn(5))) or 3 (4, fn(5), 1, fn(2))
3 (1, 2)(4, 5) or 3(4,5)(1,2)
"""

import unittest
from typing import List
from binary_tree import Tree, TreeNode


tree_vals = [3, 1, 4, 2, 5]

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


# Solution 1
def bst_sequences(nums: List[int]) -> List[List[int]]:
    tree = Tree.create_bst(tree_vals)
    root = tree.root

    def fn(node) -> List[List[int]]:
        if not node:
            return [[]]

        ret = []
        left = fn(node.left)
        right = fn(node.right)
        for seq_left in left:
            for seq_right in right:
                weave(seq_left, seq_right, [node.val], ret)
        return ret

    return fn(root)

# Solution 2: backtracking 
"""
e.g.
3 [1, 2]
3 [4, 5]

bt([3], []) -> bt([1, 4], [3]) -> bt([4, 2], [3, 1]), bt([1, 5], [3, 4]) ->
bt([2, 5], [3, 1, 4]), bt([4, 5], [3, 1, 2]) ...

steps: 
- everytime, put the node into weave array, and its left and right into next_choices with existing next choices
- parent node retires, its children succeed
"""
def bst_sequences_backtrack(nums: List[int]) -> List[List[int]]:
    tree = Tree.create_bst(tree_vals)
    root = tree.root

    ret = []
    level = 0

    # use level to trace the depth for recusion for debugging
    def backtrack(choices, weave, level = 0):
        if not choices:
            ret.append(weave)

        for i in range(len(choices)):
            # pick node to put in weave 
            node = choices[i]

            # new next choices = remaning next choices + the picked node's children
            next_choices = choices[:i] + choices[i + 1:]
            if node.left: next_choices.append(node.left)
            if node.right: next_choices.append(node.right)

            backtrack(next_choices, weave + [node.val], level + 1)

    backtrack([root], [])

    return ret




if __name__ == "__main__":
    print(bst_sequences(tree_vals))
    print(bst_sequences_backtrack(tree_vals))
    # res = []
    # weave([1, 2], [4, 5], [3], res)
    # print(res)
