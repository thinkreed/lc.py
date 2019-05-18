from collections import Counter


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0] or not word:
            return False

        board_counts = Counter(c for x in board for c in x)

        for c, count in Counter(word).items():
            if c not in board_counts or count > board_counts[c]:
                return False

        m, n = len(board), len(board[0])

        def helper(index, i, j):
            if index >= len(word):
                return True

            c = board[i][j]
            board[i][j] = ''

            if i > 0 and board[i - 1][j] == word[index] and helper(index + 1, i - 1, j):
                return True
            if i + 1 < m and board[i + 1][j] == word[index] and helper(index + 1, i + 1, j):
                return True
            if j > 0 and board[i][j - 1] == word[index] and helper(index + 1, i, j - 1):
                return True
            if j + 1 < n and board[i][j + 1] == word[index] and helper(index + 1, i, j + 1):
                return True

            board[i][j] = c
            return False

        return any(helper(1, x, y) for x in range(m) for y in range(n) if board[x][y] == word[0])
