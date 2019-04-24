class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for p in s:
            if p == '(':
                stack.append(')')
            elif p == '[':
                stack.append(']')
            elif p == '{':
                stack.append('}')
            else:
                if not stack:
                    return False
                if stack[-1] != p:
                    return False
                stack.pop()

        return len(stack) == 0
