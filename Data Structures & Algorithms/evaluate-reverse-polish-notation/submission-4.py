class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        res = 0
        # stack to store the numbers
        for token in tokens:
            if token == "+" or token == "-" or  token == "*" or token == "/":
                a = int(num_stack.pop())
                b = int(num_stack.pop())
                num_stack.append(self.calc(b, a, token))
            else:
                num_stack.append(int(token))
        return num_stack.pop()

    def calc(self, a, b, op):
        if op == "+": return a + b
        if op == "-": return a - b
        if op == "*": return a * b
        if op == "/": return int(a / b)