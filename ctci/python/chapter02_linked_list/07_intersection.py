# 2.7 - Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value.That is, if the kth
# node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.

# Keywords: identical nodes, intersection

# Solution: if two linked list intersect, then the tail nodes must be identical

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional
from linked_list import ListNode

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tail_a, tail_b = headA, headB
        len_a, len_b = 0, 0
        cur = headA
        while cur:
            tail_a = cur
            cur = cur.next
            len_a += 1
            
        cur = headB
        while cur:
            tail_b = cur
            cur = cur.next
            len_b += 1
        
        # if the tails are not identical, there is no intersection
        if tail_a is not tail_b:
            return None
        
        # make the comparsion at an equal starting point
        cur_a, cur_b, n = headA, headB, abs(len_a - len_b)
        if len_a > len_b:
            while n:
                cur_a, n = cur_a.next, n - 1
        else:
            while n:
                cur_b, n = cur_b.next, n - 1
        
        # find the first intersecting node
        while cur_a is not cur_b:
            cur_a, cur_b = cur_a.next, cur_b.next
        
        return cur_a
