# 4.5 Validate BST: Implement a function to check if a binary tree is a binary search tree.
# Hints: #35, #57, #86, #113, #128

# Keywords: inorder traversal, left <= parent<= right and min-max

import unittest

from typing import Optional
from binary_tree import TreeNode, Tree


def validate_bst_inorder(root: Optional[TreeNode]) -> bool:
    """solution 1: inorder traversal

    just keep track the value of last element, and compare with existing element
    """
    if not root:
        return True

    last_val = None

    def inorder_traversal(node):
        nonlocal last_val
        l_ret, r_ret = True, True
        if node.left:
            l_ret = inorder_traversal(node.left)
        if node and node.val is not None:
            if last_val is not None and last_val >= node.val:
                return False
            last_val = node.val
        if node.right:
            r_ret = inorder_traversal(node.right)
        return l_ret and r_ret

    return inorder_traversal(root)


def validate_bst_min_max(root: Optional[TreeNode]) -> bool:
    r"""solution 2: left <= parent <= right and min-max approach

    the min-max values is necessary for the following tree
            3
         /     \
        1       5
         \     /
          10  2 

    So the recursion knows the upper and lower bound
    """
    if not root:
        return True

    def check_bst(node, mi, ma):
        if not node:
            return True

        # check if node.val is within min-max range
        # check if left <= parent <= right
        if node.val is not None:
            # base case
            if mi and node.val <= mi:
                return False
            if ma and node.val >= ma:
                return False
            if node.left and node.left.val and node.val <= node.left.val:
                return False
            if node.right and node.right.val and node.val >= node.right.val:
                return False

            # recursion
            l_check, r_check = True, True
            if node.left:
                # for left node, need to set uppper bound
                l_check = check_bst(node.left, mi, node.val)
            if node.right:
                # for right node, need to set lower bound
                r_check = check_bst(node.right, node.val, ma)
            return l_check and r_check

        return True

    return check_bst(root, None, None)


test_cases = (
    ([2, 1, 3], True),
    ([5, 1, 4, None, None, 3, 6], False),
    ([2, 2, 2], False),
    ([0, None, -1], False),
    ([5, 4, 6, None, None, 3, 7], False),
    ([3, 1, 5, 0, 2, 4, 6, None, None, None, 3], False),
)


class Test(unittest.TestCase):
    def test_validate_bst(self):
        for tc in test_cases:
            tree_vals, expect = tc
            tree = Tree.from_list_bfs(tree_vals)
            self.assertEqual(validate_bst_inorder(tree.root), expect)
            self.assertEqual(validate_bst_min_max(tree.root), expect)


if __name__ == "__main__":
    unittest.main()
