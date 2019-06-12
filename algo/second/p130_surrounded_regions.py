class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not any(board):
            return

        m = len(board)
        n = len(board[0])

        saved = [ij for k in range(m + n) for ij in ((0, k), (m - 1, k), (k, 0), (k, n - 1))]

        while saved:
            i, j = saved.pop()

            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                saved += (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)

        for row in board:
            for i, c in enumerate(row):
                row[i] = 'XO'[c == 'S']
