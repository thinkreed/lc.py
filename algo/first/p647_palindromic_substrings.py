class Solution(object):

    def __init__(self):
        self.count = 0

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0

        for i in range(len(s)):
            self.extend_sub_palindrome(s, i, i)
            self.extend_sub_palindrome(s, i, i + 1)

        return self.count

    def extend_sub_palindrome(self, s, start, end):
        while start >= 0 and end < len(s) and (s[start] == s[end]):
            self.count += 1
            start -= 1
            end += 1
