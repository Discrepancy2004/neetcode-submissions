class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:

            if token not in ['+','-','*','/']:
                res = int(token)
                stack.append(res)

            elif token in ['+','-','*','/']:
                a = stack.pop()
                b = stack.pop()

                if token == '+':
                    stack.append(b + a)
                elif token == '-':
                    stack.append(b - a)
                elif token == '*':
                    stack.append(b * a)
                elif token == '/':
                    stack.append(int(b/a))

        return stack[-1]