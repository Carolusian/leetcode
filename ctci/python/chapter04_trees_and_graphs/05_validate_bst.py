# 4.5 Validate BST: Implement a function to check if a binary tree is a binary search tree.
# Hints: #35, #57, #86, #113, #128

# Keywords: inorder traversal, left <= parent<= right

import unittest

from typing import Optional
from binary_tree import TreeNode, Tree

def validate_bst():
    pass


test_cases = (([2, 1, 3], True), ([5, 1, 4, None, None, 3, 6], False))


class Test(unittest.TestCase):
    def test_validate_bst(self):
        pass


if __name__ == "__main__":
    for tc in test_cases:
        tree_vals, _ = tc

        tree = Tree.from_list_bfs(tree_vals)
        print(tree.root)
