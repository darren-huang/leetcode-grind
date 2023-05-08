"""Double check which edge cases are possible."""


class MinStack:
    def __init__(self):
        self.real_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.real_stack.append(val)
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.min_stack.pop()
        return self.real_stack.pop()

    def top(self) -> int:
        return self.real_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
