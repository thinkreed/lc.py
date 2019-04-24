class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        start = n * n + 1

        while start > 1:
            start, end = start - len(res), start
            res = [range(start, end)] + list(zip(*res[::-1]))

        if len(res) > 0:
            res[0] = list(res[0])

        return res


print(Solution().generateMatrix(3))
