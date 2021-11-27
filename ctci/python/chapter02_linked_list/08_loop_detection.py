# 2.8 Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.

# Keywords: slow-fast pointers

# Solution: think like a long distance race, if a man runs faster, he can be 1 lap faster

# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
# as to make a loop in the linked list.
# EXAMPLE
# Input: A -> B -> C - > D -> E -> C [the same C as earlier]
# Output: C
# Hints: #50, #69, #83, #90

import unittest
from typing import Optional
from linked_list import LinkedList, ListNode


def loop_detection(head: Optional[ListNode]) -> Optional[ListNode]:
    seen = set()
    runner = head
    while True:
        if runner in seen:
            return runner
        seen.add(runner)
        runner = runner.next


def loop_detection_slow_fast_pointers(head: Optional[ListNode]) -> Optional[ListNode]:
    slow, fast = head, head
    fast_speed = 2
    while True:
        for _ in range(fast_speed):
            fast = fast.next
            if fast is slow:
                return fast
        slow = slow.next


class Test(unittest.TestCase):
    def test_loop_detection(self):
        ll = LinkedList.from_list(["A", "B", "C", "D", "E"])
        head = ll.head
        node, n = head, 2
        while n:
            node, n = node.next, n - 1

        tail, runner = head, head
        while runner:
            tail, runner = runner, runner.next

        tail.next = node

        res = loop_detection(ll.head)
        res2 = loop_detection_slow_fast_pointers(head)
        self.assertIs(res, node)
        self.assertIs(res2, node)


if __name__ == "__main__":
    unittest.main()
