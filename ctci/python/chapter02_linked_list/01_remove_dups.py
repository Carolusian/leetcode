# Remove Dups! Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?
# keywords: double pointer
import unittest
import collections
from typing import TypeVar
from linked_list import LinkedList

T = TypeVar("T")


def remove_dups(ll: LinkedList[T]):
    # O(n)
    if not ll.head:
        return ll

    cnt = collections.Counter()
    cur = ll.head
    while cur:
        cnt[cur.val] += 1
        if cnt[cur.next.val] > 0:
            cur.next = cur.next.next
        cur = cur.next

    return ll


def remove_dups_no_buffer(ll: LinkedList[T]):
    # use two cursor with two loops: O(n^2)
    if not ll.head:
        return ll

    cur, runner = ll.head, ll.head
    while cur:
        while runner and runner.next:
            if runner.next.val == cur.val:
                runner.next = runner.next.next
            runner = runner.next
        cur, runner = cur.next, cur.next
    return ll

test_cases = (
    ([12, 11, 12, 21, 41, 43, 21], [12, 11, 21, 41, 43]),
    ([12, 11, 12, 21, 41, 43, 21, 13, 13], [12, 11, 21, 41, 43, 13]),
)

test_funcs = (remove_dups, remove_dups_no_buffer)


class Test(unittest.TestCase):
    def test_remove_dups(self):
        for tc in test_cases:
            l, expect = tc
            for fn in test_funcs:
                ll = LinkedList.from_list(l)
                self.assertEqual(fn(ll).to_list(), expect)


if __name__ == "__main__":
    unittest.main()
