import math


class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return math.floor((math.sqrt(8 * n + 1) - 1) // 2)
