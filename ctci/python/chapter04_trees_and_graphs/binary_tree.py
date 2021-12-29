# -*- coding: utf-8 -*-

r"""
root = [3,9,20,null,null,15,7]
[[3],[9,20],[15,7]]


      3
    /  \
   9    20
        / \
        15  7
According to abrove, it is constructed in BFS order
"""

import collections
import math
import unittest
from typing import List, Optional, TypeVar, Generic

T = TypeVar("T")


class TreeNode(Generic[T]):
    """define a binary tree node"""

    val: T
    left: "Optional[TreeNode[T]]"
    right: "Optional[TreeNode[T]]"
    parent: "Optional[TreeNode[T]]"

    def __init__(self, val: T, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    @property
    def height(self):
        d = collections.Counter()

        def fn(node, level):
            if node:
                if node.val is not None:
                    d[level] += 1
                if node.left:
                    fn(node.left, level + 1)
                if node.right:
                    fn(node.right, level + 1)

        fn(self, 0)
        keys = d.keys()
        if keys:
            return max(keys)
        else:
            return -1

    def __str__(self):
        h = self.height

        """
        # the bottom layer, we set every node to have 2 spaces in-between,
        n_bottom = 2 ** h - 1 - (2 ** (h - 1) - 1)
        # the length of bottom line to be printed
        bottom_line = n_bottom * 2 - (n_bottom - 1) * 1
        """

        # get the nodes for each layer
        d = collections.defaultdict(list)

        def fn(node, level):
            if node.val is not None:
                d[level].append(node.val)
            else:
                d[level].append(
                    None
                )  # if no value, we still need placeholder for display

            if node.left:
                fn(node.left, level + 1)

            if node.right:
                fn(node.right, level + 1)

        fn(self, 0)

        # get a formatted string bottom up
        bottom_up = reversed(d.values())
        lines = []
        n = 1
        for values in bottom_up:
            line = ""
            for val in values:
                if val is None:
                    line += "{0:>2}".format("")
                else:
                    line += "{0:>2}".format(val)
                # space in-between
                line += " " * 2 * n

            # prepend
            if n > 1:
                line = " " * 2 * n + line
            lines.append(line)
            n += 1

        # reverse to top-down and return
        return "\n".join(reversed(lines))


class Tree(Generic[T]):
    root: Optional[TreeNode]

    def __init__(self):
        self.root = None

    def insert(self, val, node: Optional[TreeNode[T]] = None):
        pass

    def insert_bst(self, val):
        assert self.root is not None
        
        def fn(node, val):
            if val > node.val:
                if node.right: fn(node.right, val)
                else: node.right = TreeNode(val)
            else:
                if node.left: fn(node.left, val)
                else: node.left = TreeNode(val)
        fn(self.root, val)

    @classmethod
    def create_bst(cls, l):
        tree = cls()
        tree.root = TreeNode(l[0])
        for val in l[1:]:
            tree.insert_bst(val)
        return tree

    @classmethod
    def from_list_bfs(cls, l: List[T]) -> "Tree[T]":
        """the length of binary tree nodes: 2**n - 1, construct the tree in BFS order

        solution:
          two-pointer: keep track the parent node with queue, and the leaves with iterator
        """
        if not l:
            return cls()

        it = iter(l)
        root = TreeNode(next(it))
        queue = collections.deque([root])
        while True:
            parent = queue.popleft()
            try:
                parent.left = TreeNode(next(it))
                parent.right = TreeNode(next(it))
                queue.extend([parent.left, parent.right])
            except StopIteration:
                break

        tree = cls()
        tree.root = root
        return tree

    @classmethod
    def from_list(cls, l: List[T]) -> "Tree[T]":
        """
        we can build the tree recursively base on the following attributes of a binary tree
        - the length is 2**n - 1
        - support parent index is i
        - the left child index is: 2 * i + 1
        - the right child index is: 2 * i + 2
        """

        def fn(index: int) -> TreeNode[T]:
            parent = TreeNode(l[index])
            l_index, r_index = 2 * index + 1, 2 * index + 2
            if l_index < len(l) and l[l_index] is not None:
                parent.left = fn(l_index)

            if r_index < len(l) and l[r_index] is not None:
                parent.right = fn(r_index)
            return parent

        tree = cls()
        tree.root = fn(0)
        return tree

    @classmethod
    def from_list_parent(cls, l: List[T]) -> "Tree[T]":
        """similar to from_list_bfs, but also set parent for childrens"""
        if not l:
            return cls()

        it = iter(l)
        root = TreeNode(next(it))
        queue = collections.deque([root])
        while True:
            parent = queue.popleft()
            try:
                parent.left = TreeNode(next(it), parent=parent)
                parent.right = TreeNode(next(it), parent=parent)
                queue.extend([parent.left, parent.right])
            except StopIteration:
                break

        tree = cls()
        tree.root = root
        return tree

    def to_list(self) -> List[T]:
        """get the values of a binary tree in BFS order"""
        ret = []
        queue = collections.deque([self.root])
        while queue:
            parent = queue.popleft()
            if parent:
                ret.append(parent.val)

            if parent and parent.left:
                queue.append(parent.left)

            if parent and parent.right:
                queue.append(parent.right)
        return ret


class Test(unittest.TestCase):
    def setUp(self):
        self.tree_vals = [3, 9, 20, None, None, 15, 7]

    def test_from_list(self):
        tree = Tree.from_list_bfs(self.tree_vals)
        self.assertEqual(tree.to_list(), self.tree_vals)

        tree = Tree.from_list(self.tree_vals)
        self.assertEqual(tree.to_list(), [n for n in self.tree_vals if n])

    def test_from_list_parent(self):
        tree = Tree.from_list_parent(self.tree_vals)
        self.assertEqual(tree.to_list(), self.tree_vals)

        root = tree.root

        if root and root.left:
            self.assertEqual(root.left.parent.val, 3)
        if root and root.right:
            self.assertEqual(root.right.parent.val, 3)

    def test_tree_height(self):
        tree = Tree.from_list_bfs(self.tree_vals)

        if tree.root:
            self.assertEqual(tree.root.height, 2)

    def test_print_tree(self):
        r"""
                  3
                /  \
               9    20
              / \   / \
            12  81  15  7
        """
        tree_vals = [3, 9, 20, 12, 81, 15, 7]
        tree = Tree.from_list_bfs(tree_vals)
        print(tree.root)

        tree_vals = [0, None, -1]
        tree = Tree.from_list_bfs(tree_vals)
        print(tree.root)

    def test_insert_bst(self):
        tree_vals = [3, 1, 4, 2, 5]
        tree = Tree()
        tree.root = TreeNode(tree_vals[0])

        for val in tree_vals[1:]:
            tree.insert_bst(val)
        print(tree.root)

        tree2 = Tree.create_bst(tree_vals)
        print(tree2.root)


if __name__ == "__main__":
    unittest.main()
