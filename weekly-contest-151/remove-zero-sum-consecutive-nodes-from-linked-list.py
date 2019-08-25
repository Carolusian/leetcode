"""
1171. Remove Zero Sum Consecutive Nodes from Linked List

Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

 

(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
Example 2:

Input: head = [1,2,3,-3,4]
Output: [1,2,4]
Example 3:

Input: head = [1,2,3,-3,-2]
Output: [1]
 

Constraints:

The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def remove_zeros(l):
    for i, elem in enumerate(l):
        sum = elem
        if sum == 0:
            del l[i]
            return remove_zeros(l)
        
        j = i + 1
        seq = [i]
        for next in l[i + 1:]:
            seq.append(j)
            sum += next
            sub_l = []
            if sum == 0:
                for x, elem in enumerate(l):
                    if x not in seq:
                        sub_l.append(elem)
                return remove_zeros(sub_l)
            j += 1
    return l


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        l = []
        next = head
        l.append(next.val)
        while next.next:
            next = next.next
            l.append(next.val)
        
        ret = remove_zeros(l)
        if not ret:
            return None
        
        head = ListNode(ret[0])
        next = head
        for elem in ret[1:]:
            node = ListNode(elem)
            next.next = node
            next = next.next
        return head
