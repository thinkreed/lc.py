class Solution(object):

    def __init__(self):
        self.index = 0
        self.max_len = 0

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_len = len(s)

        if s_len < 2:
            return s

        def extend_palindrome(l, r):
            while l >= 0 and r < s_len and s[l] == s[r]:
                l -= 1
                r += 1

            if self.max_len < r - l - 1:
                self.index = l + 1
                self.max_len = r - l - 1

        for i in range(s_len - 1):
            extend_palindrome(i, i)
            extend_palindrome(i, i + 1)

        return s[self.index:self.index + self.max_len]
