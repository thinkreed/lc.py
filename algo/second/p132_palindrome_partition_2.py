class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        cut = range(-1, n)

        for i in range(1, n):
            for low, high in (i, i), (i - 1, i):
                while low >= 0 and high < n and s[low] == s[high]:
                    cut[high + 1] = min(cut[high + 1], cut[low] + 1)
                    low -= 1
                    high += 1

        return cut[-1]
