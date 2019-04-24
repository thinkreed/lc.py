class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        i = 0
        j = 0

        m = len(g)
        n = len(s)

        while i < m and j < n:
            if s[j] >= g[i]:
                i += 1

            j += 1

        return i
