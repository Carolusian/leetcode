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


def sum_list(
    l1: Optional[ListNode[int]], l2: Optional[ListNode[int]]
) -> Optional[ListNode[int]]:
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


# TODO solve the same problem in forward order


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


if __name__ == "__main__":
    unittest.main()
