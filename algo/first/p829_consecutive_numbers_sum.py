class Solution:
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 1

        i = 2

        while i * (i + 1) / 2 <= N:
            if (N - i * (i + 1) / 2) % i == 0:
                res += 1
            i += 1
        return res
