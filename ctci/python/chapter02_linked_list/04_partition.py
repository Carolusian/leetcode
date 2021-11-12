# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.
# EXAMPLE
# Input:
# Output:
# 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
# 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
# Hints: #3, #24
#
# See also: https://leetcode.com/problems/partition-list/
#
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
#
# Solution:
# - shift in array is expensive, and not expensive in linked list.
# - A stable algorithm is too keep separated linked for each partition, then link them together
#
# Keywords: partition, separated list, merge, head and tail pointers, runner

import unittest
from typing import Optional, TypeVar, Any
from linked_list import LinkedList, ListNode


T = TypeVar("T", bound=int)


def partition(ll: LinkedList[T], x: T) -> LinkedList[T]:
    before_head, before_tail, after_head, after_tail = None, None, None, None
    # runner
    n = ll.head
    while n:
        if n.val < x and before_head == None:
            before_head = ListNode(n.val)
            before_tail = before_head
        elif n.val < x and before_head != None:
            before_tail.next = ListNode(n.val)
            before_tail = before_tail.next

        if n.val >= x and after_head == None:
            after_head = ListNode(n.val)
            after_tail = after_head
        elif n.val >= x and after_head != None:
            after_tail.next = ListNode(n.val)
            after_tail = after_tail.next

        n = n.next

    if not before_tail:
        return LinkedList(after_head)

    if before_tail:
        before_tail.next = after_head

    return LinkedList(before_head)


test_cases = (
    ([11, 12, 14], 10, [11, 12, 14]),
    ([1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5]),
    ([3, 5, 8, 5, 10, 2, 1], 5, [3, 2, 1, 5, 8, 5, 10]),
)


class Test(unittest.TestCase):
    def test_partition(self):
        for tc in test_cases:
            ll, x, expect = tc
            self.assertEqual(partition(LinkedList.from_list(ll), x).to_list(), expect)


if __name__ == "__main__":
    unittest.main()
