class Solution:

    def __init__(self):
        self.i = 0

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        self.i = 0

        def helper(s):
            res = ''
            n = 0

            while self.i < len(s):
                if s[self.i].isdigit():
                    while s[self.i].isdigit():
                        n = n * 10 + ord(s[self.i]) - ord('0')
                        self.i += 1
                    self.i += 1
                    extracted = helper(s)
                    while n > 0:
                        res += extracted
                        n -= 1
                elif s[self.i].isalpha():
                    res += s[self.i]
                    self.i += 1
                elif s[self.i] == ']':
                    self.i += 1
                    return res

            return res
        return helper(s)
