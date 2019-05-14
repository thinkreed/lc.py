class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r_len = len(grid)
        c_len = len(grid[0])

        for i in range(1, c_len):
            grid[0][i] += grid[0][i - 1]

        for j in range(1, r_len):
            grid[j][0] += grid[j - 1][0]

        for i in range(1, r_len):
            for j in range(1, c_len):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]
