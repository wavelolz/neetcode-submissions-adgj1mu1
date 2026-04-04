class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            # operators
            if t in ["+", "-", "*", "/"]:
                f = stack[-2]
                s = stack[-1]
                stack.pop()
                stack.pop()
                if t == "+":
                    stack.append(f+s)
                elif t == "-":
                    stack.append(f-s)
                elif t == "*":
                    stack.append(f*s)
                elif t == "/":
                    stack.append(int(f/s))
            else:
                stack.append(int(t))

        return stack[-1]

        