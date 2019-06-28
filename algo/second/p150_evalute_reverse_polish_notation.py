class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                right, left = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(left + right)
                elif token == "-":
                    stack.append(left - right)
                elif token == "*":
                    stack.append(left * right)
                else:
                    if left * right < 0 and left % right != 0:
                        stack.append(left / right + 1)
                    else:
                        stack.append(left / right)
        return stack.pop()
