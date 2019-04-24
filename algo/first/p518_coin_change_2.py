class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [1] + [0] * amount

        for i in coins:
            for j in range(i, amount + 1):
                dp[j] += dp[j - i]
        return dp[amount]
