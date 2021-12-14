# 4.6 Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
# binary search tree. You may assume that each node has a link to its parent.
# Hints: #79, #91
import unittest
from typing import Optional
from binary_tree import TreeNode, Tree

r"""
         13
        /  \
       9    20
      / \   / \
     8  11 15  23
"""
tree_vals = [13, 9, 20, 8, 11, 15, 23]  # sorted: [8, 9, 11, 13, 15, 20, 23]

def inorder_successor_v1(node: Optional[TreeNode]) -> int:
    """
    Solution:
    - find the left bottom leaf or the immediate right child; or 
    - find the immediate right parent of the left parent
    """
    if node and node.right:
        cur = node.right
        while cur.left:
            cur = cur.left
        return cur.val

    if node and node.parent and node.parent.left == node:
        cur = node.parent
        while cur and cur.parent:
            if cur.parent.left.val == cur.val:
                break
            cur = cur.parent

        return cur.val

    if node and node.parent and node.parent.right == node:
        cur = node.parent
        while cur and cur.parent:
            if cur.parent.left.val == cur.val:
                cur = cur.parent
            else:
                break
        return cur.val


def inorder_successor_v2(node: Optional[TreeNode]) -> int:
    """
    same solution enhanced

    Solution:
    - find the left bottom leaf or the immediate right child; or 
    - find the immediate right parent of itself or the left parent
    """
    if node and node.right:
        cur = node.right
        while cur.left:
            cur = cur.left
        return cur.val
    
    parent = node.parent
    child = node
    while parent and parent.right == child:  
        # if right != child, then means it is immediate right parent, and loop stop
        child = parent
        parent = parent.parent
    return parent.val



class Test(unittest.TestCase):
    def test_inorder_successor(self):
        tree = Tree.from_list_parent(tree_vals)
        root = tree.root
        # 20: if has right 
        node = root.right
        self.assertEqual(inorder_successor_v2(node), 23)
        # 8: if left node has no right, then it is parent
        node = root.left.left
        self.assertEqual(inorder_successor_v2(node), 9)

        # 11: if right node has not right, then it is right parent of parent 
        node = root.left.right
        self.assertEqual(inorder_successor_v2(node), 13)

        # 13
        node = root
        self.assertEqual(inorder_successor_v2(node), 15)
        

if __name__ == "__main__":
    unittest.main()
