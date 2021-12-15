# 4.8 First Common Ancestor: Design an algorithm and write code to find the first common ancestor
# of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
# necessarily a binary search tree.
# Hints: #70, #76, #28, #36, #46, #70, #80, #96
# 
# Keywords: LCA (lowest common ancestor), recursion
#
# Solution:
#
# See:
# - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

r"""
         13
        /  \
       9    20
      / \   / \
     8  11 15  23
"""

"""
root, p, q: 
p = 8, q = 11

lca(root, p, q)
if root.left == p and root.right == q: return root -> 9 != p 20 != q
else: lca(root.left, p, q) or lca(root.right, p, q) -> recursion

lca(root.left, p, q) -> lca(9, 8, 11) -> 9.left = 8 and 9.right = 11
"""

import unittest

tree_vals = [13, 9, 20, 8, 11, 15, 23]

if __name__ == "__main__":
    pass
