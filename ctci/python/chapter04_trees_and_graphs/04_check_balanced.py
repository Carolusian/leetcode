# 4.4 Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
# this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
# node never differ by more than one.
# Hints:#27, #33, #49, #705, #724

import unittest
from typing import Optional
from binary_tree import TreeNode, Tree

def check_balanced(root: Optional[TreeNode]) -> bool:
    if not root: return True

    l_height = 0 if not root.left else root.left.height
    r_height = 0 if not root.right else root.right.height

    print(l_height, r_height)
    if abs(l_height - r_height) > 1:
        return False

    l_check = check_balanced(root.left)
    r_check = check_balanced(root.right)
    if l_check and r_check:
        return True
    else: 
        return False


test_cases = (
    ([3, 9, 20, None, None, 15, 7], True),
    ([1, 2, 2, 3, 3, None, None, 4, 4], False),
    ([], True),
    ([1, None, 2, None, None, 3], False)
)


class Test(unittest.TestCase):
    def test_check_balanced(self):
        for tc in test_cases:
            tree_vals, expect = tc
            tree = Tree.from_list_bfs(tree_vals)
            self.assertEqual(check_balanced(tree.root), expect)


if __name__ == "__main__":
    unittest.main()
    # tree_vals = test_cases[-1][0]
    # tree = Tree.from_list_bfs(tree_vals)
    # print(tree.root)
    # check_balanced(tree.root)
