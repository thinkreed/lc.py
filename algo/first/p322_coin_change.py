class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        maximum = amount + 1
        dp = [maximum] * maximum
        dp[0] = 0

        for i in range(1, maximum):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        return -1 if dp[amount] > amount else dp[amount]
