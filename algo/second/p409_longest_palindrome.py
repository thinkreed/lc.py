from collections import Counter


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = sum(c & ~1 for c in Counter(s).values())

        return count + (count < len(s))
