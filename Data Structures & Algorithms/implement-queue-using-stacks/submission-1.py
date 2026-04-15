class MyQueue:

    def __init__(self):
        self.stack = []
        self.helper_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.helper_stack:
            for _ in range(len(self.stack)):
                self.helper_stack.append(self.stack.pop())
        return self.helper_stack.pop()
    def peek(self) -> int:
        if not self.helper_stack:
            for _ in range(len(self.stack)):
                self.helper_stack.append(self.stack.pop())
        return self.helper_stack[-1]

    def empty(self) -> bool:
        return max(len(self.stack),len(self.helper_stack)) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()