# Stack Min: How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.

# Keywords: temporary array

# Solution: use another list to store min values

# See: https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.data = []
        self.minval = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if not self.minval or self.minval[-1] >= val:
            self.minval.append(val)

    def pop(self) -> None:
        val = self.data.pop()
        if val == self.minval[-1]:
            self.minval.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.minval[-1]
