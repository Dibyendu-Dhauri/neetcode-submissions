class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch == '+':
                stack.append(stack.pop() + stack.pop())
            elif ch == '*':
                stack.append(stack.pop() * stack.pop())
            elif ch == '/':
                first_operands = stack.pop()
                second_operands = stack.pop()
                # stack.append(second_operands // first_operands)
                stack.append(int(second_operands / first_operands))
            elif ch == '-':
                first_operands = stack.pop()
                second_operands = stack.pop()
                stack.append(second_operands - first_operands)
            else:
                stack.append(int(ch))
        return stack[0]

            