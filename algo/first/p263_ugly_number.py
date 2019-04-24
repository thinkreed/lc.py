class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for prime_factor in 2, 3, 5:
            while num % prime_factor == 0 < num:
                num /= prime_factor

        return num == 1
