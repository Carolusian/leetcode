# -*- coding: utf-8 -*-

r"""
root = [3,9,20,null,null,15,7]
[[3],[9,20],[15,7]]


   3
  / \
 9   20
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

    def __init__(self, val: T):
        self.val = val
        self.left = None
        self.right = None


class Tree(Generic[T]):
    def __init__(self):
        self.root = None

    def insert(self, val, node: Optional[TreeNode[T]] = None):
        pass

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
        we can build the tree recursively base the following attributes of a binary tree
        - the length is 2**n - 1
        - support parent index is i
        - the left child index is: 2 * i + 1
        - the right child index is: 2 * i + 2
        """
        def fn(index: int) -> TreeNode[T]:
            parent = TreeNode(l[index])
            l_index, r_index = 2 * index + 1, 2 * index + 2
            if l_index < len(l) and l[l_index]:
                parent.left = fn(l_index)

            if r_index < len(l) and l[r_index]:
                parent.right = fn(r_index)
            return parent


        tree = cls()
        tree.root = fn(0)
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
    def test_from_list(self):
        tree_vals = [3, 9, 20, None, None, 15, 7]

        tree = Tree.from_list_bfs(tree_vals)
        self.assertEqual(tree.to_list(), tree_vals)

        tree = Tree.from_list(tree_vals)
        self.assertEqual(tree.to_list(), [n for n in tree_vals if n])
        

if __name__ == "__main__":
    unittest.main()
   
