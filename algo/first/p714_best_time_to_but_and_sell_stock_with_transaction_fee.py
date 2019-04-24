class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        no_stock = 0
        have_stock = float('-inf')

        for price in prices:
            old_profit = no_stock
            no_stock = max(no_stock, have_stock + price - fee)
            have_stock = max(have_stock, old_profit - price)

        return no_stock
