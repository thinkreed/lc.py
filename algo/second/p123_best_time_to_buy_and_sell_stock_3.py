class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        hold1 = float('-inf')
        hold2 = float('-inf')

        release1 = 0
        release2 = 0

        for i in prices:
            release2 = max(release2, hold2 + i)
            hold2 = max(hold2, release1 - i)
            release1 = max(release1, hold1 + i)
            hold1 = max(hold1, -i)

        return release2
