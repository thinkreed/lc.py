class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def dfs_marking(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] != '1':
                return

            grid[i][j] = '0'
            dfs_marking(i + 1, j)
            dfs_marking(i - 1, j)
            dfs_marking(i, j + 1)
            dfs_marking(i, j - 1)

        res = 0
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs_marking(i, j)
                    res += 1
        return res
