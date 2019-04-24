from math import sqrt


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c < 0:
            return False

        left = 0
        right = int(sqrt(c))

        while left <= right:
            cur = left * left + right * right

            if cur < c:
                left += 1
            elif cur > c:
                right -= 1
            else:
                return True

        return False
