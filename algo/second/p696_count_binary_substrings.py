class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = map(len, s.replace('01', '0 1').replace('10', '1 0').split())
        return sum(min(x, y) for x, y in zip(tmp, tmp[1:]))
