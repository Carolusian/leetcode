# 2.6 Palindrome: Implement a function to check if a linked list is a palindrome.
# Keywords: palindrome, reverse, recursion, recursive, reverse half
# Solution 1: use a array, then compare array and reversed array

# Solution 2: compare recursively

# Solution 3: reverse the second half, then compare the value of two pointer

import unittest
from linked_list import ListNode, LinkedList
from typing import Optional


def is_palindrome(head: Optional[ListNode]) -> bool:
    return True


test_cases = (([1, 2, 2, 1], True), ([1, 2], False))


class Test(unittest.TestCase):
    def test_is_palindrome(self):
        for tc in test_cases:
            l, expect = tc
            ll = LinkedList.from_list(l)
            self.assertEqual(is_palindrome(ll.head), expect)


if __name__ == "__main__":
    unittest.main()
