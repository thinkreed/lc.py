class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        do_sell = 0
        do_buy = -prices[0]
        prev_sell = 0
        prev_buy = 0

        for price in prices:
            prev_buy = do_buy
            do_buy = max(prev_sell - price, prev_buy)
            prev_sell = do_sell
            do_sell = max(prev_buy + price, prev_sell)

        return do_sell
