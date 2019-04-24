class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        def helper(i, j):
            adj = (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)
            res = 0

            for x, y in adj:
                if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y] == 0:
                    res += 1

            return res

        ret = 0
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 1:
                    ret += helper(m, n)

        return ret
