# 2.6 Palindrome: Implement a function to check if a linked list is a palindrome.
# Keywords: palindrome, reverse, recursion, recursive before base case, reverse half
# Solution 1: use a array, then compare array and reversed array

# Solution 2: compare recursively, if base case if after recursion, then it is proceeded in reverse order

# Solution 3: reverse the second half, then compare the value of two pointer

import math
import unittest
from linked_list import ListNode, LinkedList
from typing import Optional


class Solution:
    def is_palindrome_recursive(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        self.ptr = head

        def reverse_check(node: Optional[ListNode]):
            global ptr
            if node and not reverse_check(node.next):
                return False
            if node and self.ptr.val != node.val:
                return False
            if node and self.ptr.val == node.val:
                self.ptr = self.ptr.next
            return True

        return reverse_check(self.ptr)


def is_palindrome_2nd_half_reverse(head: Optional[ListNode]) -> bool:
    # linked list reverse helper function: for the purpose to reverse second half
    def reverse_linkedlist(head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev, cur = None, head
        while cur:
            prev, cur.next, cur = cur, prev, cur.next
        return prev

    if not head:
        return False

    # move to second half
    half = math.ceil(len(head) / 2)
    prev, runner = None, head
    while runner and half:
        prev, runner, half = runner, runner.next, half - 1

    # connect to the second half
    prev.next = reverse_linkedlist(runner)

    # compare
    p1, p2, n = head, prev.next, len(head) // 2
    while n:
        if p1.val != p2.val:
            return False
        p1, p2, n = p1.next, p2.next, n - 1

    return True


sol = Solution()
test_cases = (([1, 2, 2, 1], True), ([1, 2], False))
test_funcs = (sol.is_palindrome_recursive, is_palindrome_2nd_half_reverse)


class Test(unittest.TestCase):
    def test_is_palindrome(self):
        for tc in test_cases:
            for func in test_funcs:
                l, expect = tc
                ll = LinkedList.from_list(l)
                self.assertEqual(func(ll.head), expect)


if __name__ == "__main__":
    unittest.main()
