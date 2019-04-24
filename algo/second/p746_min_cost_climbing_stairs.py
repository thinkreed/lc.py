class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)

        if n == 0 or n == 1:
            return 0

        a = cost[0]
        b = cost[1]

        for i in range(2, n):
            a, b = b, min(a, b) + cost[i]

        return min(a, b)
