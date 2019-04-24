class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        res = 0
        heads = 0
        tails = 0

        for num in A:
            if L <= num <= R:
                heads += tails + 1
                tails = 0
                res += heads
            elif num < L:
                tails += 1
                res += heads
            else:
                heads = 0
                tails = 0

        return res
