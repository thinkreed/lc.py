class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ordered_t = iter(t)
        return all(c in ordered_t for c in s)

    def is_subsequence(self, s, t):
        last = -1
        for c in s:
            index = t.find(c, last + 1)
            if index == -1:
                return False
            last = index

        return True
