class MyQueue:

    def __init__(self):
        self.stack = []
        self.helper_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        for _ in range(len(self.stack) - 1):
            self.helper_stack.append(self.stack.pop())
        ans =  self.stack.pop()

        for _ in range(len(self.helper_stack)):
            self.stack.append(self.helper_stack.pop())
        return ans
    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()