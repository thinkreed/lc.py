class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        step = 0

        for i in range(2, n + 1):
            while n % i == 0:
                step += i
                n //= i

        return step
