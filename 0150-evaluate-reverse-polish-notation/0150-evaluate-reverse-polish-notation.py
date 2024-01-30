class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        

        for token in tokens:
            # if the token is not an operand, push it in the stack
            if token not in '+-*/':
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.append(a+b)
                elif token == '-':
                    stack.append(a-b)
                elif token == '*':
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
            
        return stack.pop()