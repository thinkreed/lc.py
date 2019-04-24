class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + [n for n in nums if n > 0] + [1]
        n = len(nums)

        dp = [[0] * n for x in range(n)]

        for i in range(2, n):
            for j in range(0, n - i):
                r = j + i

                for k in range(j + 1, r):
                    dp[j][r] = max(dp[j][r], nums[j] * nums[k] * nums[r] + dp[j][k] + dp[k][r])

        return dp[0][n - 1]
