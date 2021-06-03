import unittest


class ThreeStacks:
    def __init__(self):
        self.array = [None, None, None]
        self.current = [0, 1, 2]

    def push(self, item, stack_number):
        if stack_number not in [0, 1, 2]:
            raise Exception("Bad stack number")

        # extend the capacity when exceeding
        while len(self.array) <= self.current[stack_number]:
            self.array += [None] * len(self.array)

        self.array[self.current[stack_number]] = item
        self.current[stack_number] += 3

    def pop(self, stack_number):
        if stack_number not in [0, 1, 2]:
            raise Exception("Bad stack number")

        if self.current[stack_number] > 3:
            self.current[stack_number] -= 3

        item = self.array[self.current[stack_number]]
        self.array[self.current[stack_number]] = None
        return item


class Test(unittest.TestCase):
    def test_three_stacks(self):
        three_stacks = ThreeStacks()
        three_stacks.push(101, 0)
        three_stacks.push(102, 0)
        three_stacks.push(103, 0)
        three_stacks.push(201, 1)
        print(three_stacks.array)
        print(three_stacks.current)


if __name__ == "__main__":
    unittest.main()
