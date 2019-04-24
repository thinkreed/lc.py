import heapq


class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        h = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        res = 0

        while True:
            t, x, y = heapq.heappop(h)
            res = max(res, t)

            if x == y == n - 1:
                return res

            for i, j in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if 0 <= i < n and 0 <= j < n and (i, j) not in visited:
                    visited.add((i, j))
                    heapq.heappush(h, (grid[i][j], i, j))
