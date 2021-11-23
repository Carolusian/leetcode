# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
# EXAMPLE
# lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
# Output: 9 - > 1 -> 2. That is, 912.
# Hints: #7, #30, #71, #95, #109

# keywords: math, carry, reminder, addition, padding when different length, recursion for smaller, insert before

# See:
# - https://leetcode.com/problems/add-two-numbers/
# - https://leetcode.com/problems/add-two-numbers-ii/

import unittest
from typing import Optional
from linked_list import LinkedList, ListNode


test_cases = (
    ([7, 1, 6], [5, 9, 2], [2, 1, 9]),
    ([0], [0], [0]),
    ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
)

test_cases_forword_order = (
    ([6, 1, 7], [2, 9, 5], [9, 1, 2]),
    ([0], [0], [0]),
    ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [1, 0, 0, 0, 9, 9, 9, 8]),
)


def sum_list(l1: Optional[ListNode[int]], l2: Optional[ListNode[int]]) -> Optional[ListNode[int]]:
    n1, n2, carry = l1, l2, 0
    head, runner = None, None
    while n1 or n2 or carry:
        v1 = n1.val if n1 else 0
        v2 = n2.val if n2 else 0

        total = v1 + v2 + carry
        carry = total // 10
        num = total % 10

        if n1:
            n1 = n1.next
        if n2:
            n2 = n2.next

        if not head:
            head = ListNode(num)
            runner = head
        else:
            runner.next = ListNode(num)
            runner = runner.next

    return head


# Alternated problem: solve the same problem in forward order
def sum_list_forward_order(
    l1: Optional[ListNode[int]], l2: Optional[ListNode[int]]
) -> Optional[ListNode[int]]:
    # NOTES:
    # for forward order list, need to padding zero to the shorter list
    # sum the next node firsts,
    # then sum the current nodes with the carry from the sum of the sum of the next nodes
    def pad_zero(l: ListNode[int], n: int):
        head = l
        for _ in range(n):
            node = ListNode(0)
            node.next = head
            head = node
        return head

    def partial_sum(ln1: Optional[ListNode[int]], ln2: Optional[ListNode[int]]):
        # the length of ln1 and ln2 is equal now
        n1, n2, carry, next_sum_node = ln1, ln2, 0, None
        if n1.next and n2.next:
            next_sum_node, carry = partial_sum(n1.next, n2.next)

        total = carry + n1.val + n2.val
        carry = total // 10
        sum = total % 10
        sum_node = ListNode(sum)
        sum_node.next = next_sum_node
        return sum_node, carry

    if len(l1) <= len(l2):
        l1 = pad_zero(l1, len(l2) - len(l1))
    else:
        l2 = pad_zero(l2, len(l1) - len(l2))

    res, carry = partial_sum(l1, l2)
    if carry > 0:
        head = ListNode(carry)
        head.next = res
        return head

    return res


class Test(unittest.TestCase):
    def test_sum_list(self):
        for tc in test_cases:
            l1 = LinkedList.from_list(tc[0])
            l2 = LinkedList.from_list(tc[1])
            expect = tc[2]
            res = sum_list(l1.head, l2.head)
            if res:
                ll = LinkedList()
                ll.head = res
                self.assertEqual(ll.to_list(), expect)

        for tc in test_cases_forword_order:
            l1 = LinkedList.from_list(tc[0])
            l2 = LinkedList.from_list(tc[1])
            expect = tc[2]
            res = sum_list_forward_order(l1.head, l2.head)
            if res:
                ll = LinkedList()
                ll.head = res
                self.assertEqual(ll.to_list(), expect)


if __name__ == "__main__":
    unittest.main()
    # ll1 = LinkedList.from_list([1, 2])
    # ll2 = LinkedList.from_list([2, 3, 4])
    # sum_list_forward_order(ll1.head, ll2.head)
