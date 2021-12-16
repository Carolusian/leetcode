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
import collections
from binary_tree import Tree, TreeNode

tree_vals = [13, 9, 20, 8, 11, 15, 23]


# more commonly named as LCA: lowest common ancestor
# method 1: find paths from root to both p and q, then find the same ancestor in the paths
def lca1(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    paths = collections.defaultdict(list)

    def fn(node, child):
        if not node:
            return None

        if node.val == child.val:
            paths[child.val].append(node)
            return node

        if (node.left and fn(node.left, child)) or (
            node.right and fn(node.right, child)
        ):
            paths[child.val].append(node)
            return node

    fn(root, p)
    fn(root, q)

    for n in paths[p.val]:
        for m in paths[q.val]:
            if n.val == m.val:
                return n
    return root


# method 2: if both node.left and node.right does not return None, then node is LCA
def lca2(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # edge case: find the real root, if root does not have children on both sides
    while not root.left or not root.right:
        if root.left:
            root = root.left
        elif root.right:
            root = root.right

    def fn(node, p, q):
        if not node:
            return None

        if node in (p, q):
            return node

        left, right = fn(node.left, p, q), fn(node.right, p, q)
        if left and right:
            return node
        return left or right

    return fn(root, p, q) or root


class Test(unittest.TestCase):
    def test_lca(self):
        tree = Tree.from_list_bfs(tree_vals)
        root = tree.root

        assert root != None and root.left and root.right
        self.assertEqual(lca1(root, root.left, root.right), root)
        self.assertEqual(lca2(root, root.left, root.right), root)

        assert root != None and root.left.right and root.left.left
        self.assertEqual(lca1(root, root.left.right, root.left.left), root.left)
        self.assertEqual(lca2(root, root.left.right, root.left.left), root.left)


if __name__ == "__main__":
    unittest.main()
