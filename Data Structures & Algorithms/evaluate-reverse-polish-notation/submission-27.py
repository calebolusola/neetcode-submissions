import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ["+", "-", "*", "/"]
        # tokens = ["1","2","+","3","*","4","-"]
        # iterate through tokens, check if i is an operand. If i is not an operand, then append it to the stack. if it is, pop the last 2 items from the stack, operate on them with the operand, then append it back to the stack. Once you've gone through the entire tokens, then return the only element remaining

        for i in tokens:
            if i not in operands or not stack:
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                if i == "+":
                    stack.append(b+a)
                elif i == "-":
                    stack.append(b-a)
                elif i == "*":
                    stack.append(b*a)
                elif i == "/":
                    stack.append(int(b/a))

        return stack[0]