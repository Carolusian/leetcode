# 3.4 Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
# Hints: #98, #7 74

# Solution: one stack is used to push elems, another stack for poping elems

# See: https://leetcode.com/problems/implement-queue-using-stacks/

from collections import deque

class MyQueue:

    def __init__(self):
        self.push_stack = deque()
        self.pop_stack = deque()
        
    def push(self, x: int) -> None:
        self.push_stack.append(x)

    def pop(self) -> int:
        if self.pop_stack:
            return self.pop_stack.pop()
        elif self.push_stack:
            self.refill_pop_stack()
            return self.pop_stack.pop()
        return -1
        
    def peek(self) -> int:
        if self.pop_stack:
            return self.pop_stack[-1]
        elif self.push_stack:
            self.refill_pop_stack()
            return self.pop_stack[-1]
        return -1
        
    def empty(self) -> bool:
        return not self.push_stack and not self.pop_stack
        
    def refill_pop_stack(self):
        while self.push_stack:
            self.pop_stack.append(self.push_stack.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
