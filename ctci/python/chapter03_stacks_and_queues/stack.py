from typing import Optional, List, TypeVar, Generic
import unittest


T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self, data: List[T] = []):
        self.data = data


    def push(self, val: T):
        self.data.append(val)


    def pop(self) -> T:
        return self.data.pop()


    def empty(self) -> bool:
        return not self.data


class Test(unittest.TestCase):
    def test_stack(self):
        stack = Stack()

        stack.push(1)
        self.assertEqual(stack.data, [1])

        stack.push(2)
        self.assertEqual(stack.pop(), 2)

        self.assertFalse(stack.empty())

        stack.pop()
        self.assertTrue(stack.empty())


if __name__ == "__main__":
    unittest.main()
