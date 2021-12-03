# 3.3 Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
# (that is, pop () should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt ( int index) which performs a pop operation on a specific sub-stack.
# Hints:#64, #87

# Keywords: min(multiple cursors)

# See: https://leetcode.com/problems/dinner-plate-stacks/

import collections


class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.stacks = []
        self.curs = []  # indices of stacks not yet full

    def push(self, val: int) -> None:
        if self.capacity * len(self.stacks) == self.length:
            self.stacks.append(collections.deque([val]))
            if not len(self.stacks[-1]) == self.capacity:
                self.curs.append(len(self.stacks) - 1)
        else:
            cur = min(self.curs)
            self.stacks[cur].append(val)
            if len(self.stacks[cur]) == self.capacity:
                self.curs.remove(cur)
        self.length += 1
        

    def pop(self) -> int:
        if not self.length:
            return -1
        
        # If popping from the last stack, 
        # and the stack becomes empty, always remove it
        idx = len(self.stacks) - 1
        while not self.stacks[idx]:
            del self.stacks[idx]
            idx = idx - 1
            
        ret = self.stacks[idx].pop()
        
        if not self.stacks[idx]:
            del self.stacks[idx]
            if (idx) in self.curs:
                self.curs.remove(idx)
            idx = idx - 1
        

        if idx >= 0 and idx < len(self.stacks) and len(self.stacks[idx]) < self.capacity and idx not in self.curs:
            self.curs.append(idx)
            
        self.length -= 1
        return ret
        
    def popAtStack(self, index: int) -> int:
        if not self.length or index > len(self.stacks) - 1 or not self.stacks[index]:
            return -1
        
        # if popping from last stack
        if index == len(self.stacks) - 1:
            return self.pop()
        
        # if not popping from last stack
        ret = self.stacks[index].pop()
        self.length -= 1
        
        if index not in self.curs:
            self.curs.append(index)
        
        return ret


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
