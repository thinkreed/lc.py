class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        cur = 0

        for i in range(1, len(prices)):
            cur = cur + prices[i] - prices[i - 1]
            cur = max(0, cur)
            res = max(res, cur)

        return res
