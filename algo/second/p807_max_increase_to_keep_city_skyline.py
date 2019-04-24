class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        row = map(max, grid)
        col = map(max, zip(*grid))

        res = 0
        n = len(grid)

        for i in range(n):
            for j in range(n):
                res += min(row[i], col[j]) - grid[i][j]

        return res
