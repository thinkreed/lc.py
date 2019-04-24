class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        grid = [[N] * N for _ in range(N)]

        for mine in mines:
            grid[mine[0]][mine[1]] = 0

        for i in range(N):
            left = 0
            right = 0
            up = 0
            down = 0

            for j, k in zip(range(N), reversed(range(N))):
                left = left + 1 if grid[i][j] != 0 else 0
                if left < grid[i][j]:
                    grid[i][j] = left

                right = right + 1 if grid[i][k] != 0 else 0
                if right < grid[i][k]:
                    grid[i][k] = right

                up = up + 1 if grid[j][i] != 0 else 0
                if up < grid[j][i]:
                    grid[j][i] = up

                down = down + 1 if grid[k][i] != 0 else 0
                if down < grid[k][i]:
                    grid[k][i] = down

        res = 0

        for i in range(N):
            for j in range(N):
                if res < grid[i][j]:
                    res = grid[i][j]

        return res
