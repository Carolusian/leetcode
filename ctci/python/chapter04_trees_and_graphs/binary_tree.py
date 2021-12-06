# -*- coding: utf-8 -*-
from typing import Optional, TypeVar

# T = TypeVar("T")

class TreeNode:
    """define a binary tree node"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, val, node: Optional[TreeNode] = None):
        pass
    
