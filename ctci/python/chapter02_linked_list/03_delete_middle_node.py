# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node., the node is not the tail node
# EXAMPLE
# lnput:the node c from the linked list: a->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like: a->b->d->e->f
# Hints:#72
#
# keywords: replace value in node
# Solution: since the head of the linked list is not give, we cannot get the previous node, so we cannot delete the given node directly.
#   thus, we shall replace the value of current node with the value in the next ndoe, then delete next node

import unittest
from typing import Optional
from linked_list import LinkedList, ListNode


def delete_middle_node(n: Optional[ListNode]):
    if n and n.next:
        n.val = n.next.val
        n.next = n.next.next


test_cases = (
    (["a", "b", "c", "d", "e", "f"], "c", ["a", "b", "d", "e", "f"]),
    (["a", "b", "c", "d", "e", "f"], "e", ["a", "b", "c", "d", "f"]),
)


class Test(unittest.TestCase):
    def test_delete_middle_node(self):
        for tc in test_cases:
            l, val, expect = tc
            ll = LinkedList.from_list(l)
            n = ll.head
            while n.val != val and n.next:
                n = n.next
            delete_middle_node(n)
            self.assertEqual(ll.to_list(), expect)


if __name__ == "__main__":
    unittest.main()
