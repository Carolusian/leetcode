# implement basic linked list: factory and traverse methods
from typing import Generic, Optional, TypeVar, Sequence, Iterable
import unittest

T = TypeVar("T")


class ListNode(Generic[T]):
    val: T
    next: Optional["ListNode[T]"]

    def __init__(self, val: T, next: Optional["ListNode[T]"] = None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)


class LinkedList(Generic[T]):
    """A linked list in essence is just the head node"""

    head: Optional[ListNode[T]]

    def __iter__(self) -> Iterable[ListNode[T]]:
        it = self.head
        while it:
            yield it
            it = it.next

    @classmethod
    def from_list(cls, lst: Sequence[T]):
        ll = cls()

        if len(lst) > 0:
            ll.head = ListNode(lst[0])
            cur = ll.head
            for it in lst[1:]:
                cur.next = ListNode(it)
                cur = cur.next

        return ll


class Test(unittest.TestCase):
    def test_linked_list(self):
        ll = LinkedList.from_list([1, 2, 3])
        res = [node.val for node in ll if node]
        self.assertEqual(res, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
