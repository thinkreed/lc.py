class Solution(object):

    def __init__(self):
        self.low = 0
        self.m_len = 0

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def extend_palindrome(j, k):
            while j >= 0 and k < len(s) and s[j] == s[k]:
                j -= 1
                k += 1

            if self.m_len < k - j - 1:
                self.low = j + 1
                self.m_len = k - j - 1

        l = len(s)

        if l < 2:
            return s

        for i in range(l - 1):
            extend_palindrome(i, i)
            extend_palindrome(i, i + 1)

        return s[self.low:self.low + self.m_len]
