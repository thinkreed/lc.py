class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def live_neighbors(i, j):
            count = 0
            for x in range(max(i - 1, 0), min(i + 1, m - 1) + 1):
                for y in range(max(j - 1, 0), min(j + 1, n - 1) + 1):
                    count += board[x][y] & 1
            count -= board[i][j] & 1
            return count

        if board is None or len(board) == 0:
            return

        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                lives = live_neighbors(i, j)
                if board[i][j] == 1 and 2 <= lives <= 3:
                    board[i][j] = 3
                if board[i][j] == 0 and lives == 3:
                    board[i][j] = 2

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
