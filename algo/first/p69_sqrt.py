class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = x
        while result * result > x:
            result = (result + x // result) // 2

        return result
