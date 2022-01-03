# 4.10 Check Subtree: Tl and T2 are two very large binary trees, with Tl much bigger than T2. Create an
# algorithm to determine if T2 is a subtree of Tl.
# A tree T2 is a subtree of Tl if there exists a node n in Tl such that the subtree of n is identical to T2.
# That is, if you cut off the tree at node n, the two trees would be identical.
# Hints:#4, #11, #18, #31, #37

# Keywords: BFS, compare children recursively
# Solution: two small problems: search subroot in root; compare if two trees are equal

import unittest
import collections
from typing import Optional

from binary_tree import Tree, TreeNode


def search_node(
    root: Optional[TreeNode], search_node: Optional[TreeNode]
) -> Optional[TreeNode]:
    """BFS search"""
    if not root or not search_node:
        return None

    queue = collections.deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        if node.val == search_node.val:
            return node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return None


def compare_trees(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
    """compare each node recursively"""
    if not node1 and not node2:
        return True
    elif not node1 or not node2:
        return False

    if node1.val != node2.val:
        return False

    return compare_trees(node1.left, node2.left) and compare_trees(
        node1.right, node2.right
    )


def check_subtree(root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
    node = search_node(root, subroot)
    if not node:
        return False

    return compare_trees(node, subroot)


r"""
    3
   / \
  4   5
 / \
1   2


  4
 / \
1   2
"""

test_cases = (
    ([3, 4, 5, 1, 2], [4, 1, 2], True),
    ([3, 4, 5, 1, 2], [4, 1, 2, None, None, None, 0], False),
)


class Test(unittest.TestCase):
    def test_check_subtree(self):
        for tc in test_cases:
            t1, t2, expect = tc
            tree1, tree2 = Tree.from_list(t1), Tree.from_list(t2)
            self.assertEqual(check_subtree(tree1.root, tree2.root), expect)


if __name__ == "__main__":
    unittest.main()
