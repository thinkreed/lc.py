class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        def dfs(x, y, pre, preval):
            if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] < pre or (
                    visited[x][y] & preval) == preval:
                return
            visited[x][y] |= preval
            if visited[x][y] == 3:
                res.append((x, y))
            dfs(x + 1, y, matrix[x][y], visited[x][y])
            dfs(x - 1, y, matrix[x][y], visited[x][y])
            dfs(x, y + 1, matrix[x][y], visited[x][y])
            dfs(x, y - 1, matrix[x][y], visited[x][y])

        res = []
        if not matrix:
            return res

        m = len(matrix)
        n = len(matrix[0])
        visited = [[0] * n for _ in range(m)]

        for i in range(m):
            dfs(i, 0, float('-inf'), 1)
            dfs(i, n - 1, float('-inf'), 2)
        for i in range(n):
            dfs(0, i, float('-inf'), 1)
            dfs(m - 1, i, float('-inf'), 2)

        return res
