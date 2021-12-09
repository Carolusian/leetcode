# List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
# at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
# Hints: #107, #123, #135

# Keywords: traversal, tree height
# Solution: if the level has nodes, add it the counter of that level

import collections
import unittest
from binary_tree import TreeNode, Tree


def list_of_depths(root: TreeNode[int]):
    d = collections.defaultdict(list)
    def tree_traversal(node, level):
        if not node or not node.val:
            return

        d[level].append(node.val)
        tree_traversal(node.left, level + 1)
        tree_traversal(node.right, level + 1)

    tree_traversal(root, 0)
    return [v for _, v in d.items()]

    

test_case = ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]])


class Test(unittest.TestCase):
    def test_list_of_depths(self):
        values, expect = test_case
        tree = Tree.from_list_bfs(values)
        root = tree.root
        if not root:
            return 

        self.assertEqual(list_of_depths(root), expect)


if __name__ == "__main__":
    unittest.main()
