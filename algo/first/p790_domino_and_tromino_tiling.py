class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        md = 10 ** 9
        md += 7
        dp = [0] * 1001
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        if N <= 3:
            return dp[N]

        for i in range(4, N + 1):
            dp[i] = 2 * dp[i - 1] + dp[i - 3]
            dp[i] %= md

        return dp[N]
