# 2096. Step-By-Step Directions From a Binary Tree Node to Another

# Solution: first, find lowest common ancestor of start and end node, then find the path from the ancestor to both startValue and destValue
# Keywords: LCA, Lowest Common Ancestor
# See: https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# User Accepted:1714
# User Tried:2600
# Total Accepted:1757
# Total Submissions:5635
# Difficulty:Medium
# You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.
#
# Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:
#
# 'L' means to go from a node to its left child node.
# 'R' means to go from a node to its right child node.
# 'U' means to go from a node to its parent node.
# Return the step-by-step directions of the shortest path from node s to node t.
#
#
#
# Example 1:
#
#
# Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
# Output: "UURL"
# Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
# Example 2:
#
#
# Input: root = [2,1], startValue = 2, destValue = 1
# Output: "L"
# Explanation: The shortest path is: 2 → 1.
#
#
# Constraints:
#
# The number of nodes in the tree is n.
# 2 <= n <= 105
# 1 <= Node.val <= n
# All the values in the tree are unique.
# 1 <= startValue, destValue <= n
# startValue != destValue

from typing import Optional, List, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        def lca(node: Optional[TreeNode]):
            """get lowest common ancestor of node with startValue and destValue"""
            if not node or node.val in (startValue, destValue):
                return node
            left, right = lca(node.left), lca(node.right)

            # if both left and right is not None, then common ancestor is the node
            # otherwise, it is in the left or right branches
            return node if left and right else left or right

        root = lca(root)

        def fn(val):
            # find the path from root to val
            stack: List[Tuple[Optional[TreeNode], str]] = [(root, "")]
            while stack:
                node, path = stack.pop()
                if node and node.val == val:
                    return path
                if node and node.left:
                    stack.append((node.left, path + "L"))
                if node and node.right:
                    stack.append((node.right, path + "R"))
            return ""

        path0 = fn(startValue)
        path1 = fn(destValue)
        return "U" * len(path0) + path1
