class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        s_len, t_len = len(s) + 1, len(t) + 1
        cur = [0] * t_len
        cur[0] = 1
        for i in xrange(1, s_len):
            pre = cur[:]
            for j in xrange(1, t_len):
                cur[j] = pre[j] + pre[j - 1] * (s[i - 1] == t[j - 1])
        return cur[-1]