class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a = n ^ (n / 2)
        b = a + 1
        return not (a & b)
