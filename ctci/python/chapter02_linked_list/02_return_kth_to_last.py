# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
#
# Reference: leetcode: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#
# Solutions 1: two pass, one pass count all, the calculated according to the length and n
# Solution 2: one pass, two cursors/pointers, one fast, one slow, keep the distance between the two to be n

import unittest
from typing import Optional, TypeVar
from linked_list import ListNode, LinkedList

T = TypeVar("T")


def nth_to_last(head: Optional[ListNode[T]], n: int) -> Optional[T]:
    if not head:
        return None
    elif not head.next:
        return head.val

    node, cnt = head, 0
    while node.next:
        node = node.next
        cnt += 1

    node = head
    for _ in range(cnt - n + 1):
        node = node.next
    if node:
        return node.val
    return None


def nth_to_last_one_pass(head: Optional[ListNode[T]], n: int) -> Optional[T]:
    if not head:
        return None
    elif not head.next:
        return head.val

    # the case of two nodes
    n1, n2, dist, cnt = head, head.next, 1, 2
    while n2.next:
        n2 = n2.next
        if dist >= n:
            n1 = n1.next
        else:
            dist += 1
        cnt += 1

    # if n1 not moved, nth to the last is the head
    if n == cnt and head == n1:
        return n1.val

    return n1.next.val


tc = (
    ([1, 2, 3, 4, 5], 2, 4),
    ([1], 1, 1),
    ([1, 2, 3], 2, 2),
    ([1, 2], 1, 2),
    ([1, 2], 2, 1),
)

funcs = (nth_to_last, nth_to_last_one_pass)


class Test(unittest.TestCase):
    def test_kth_to_last(self):
        for c in tc:
            lst, n, expect = c
            ll = LinkedList.from_list(lst)
            for func in funcs:
                self.assertEqual(func(ll.head, n), expect)


if __name__ == "__main__":
    unittest.main()
    # ll = LinkedList.from_list(tc[0][0])
    # kth_to_last_one_pass(ll.head, 2)
