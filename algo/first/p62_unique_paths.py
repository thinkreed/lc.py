class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1 for _ in range(n)] for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]

    def unique_paths(self, m, n):
        down_steps = m - 1
        total_steps = m - 1 + n - 1

        res = 1

        for i in range(1, down_steps + 1):
            res = res * (total_steps - down_steps + i) // i

        return res
