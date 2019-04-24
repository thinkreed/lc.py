class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        rows = len(board)
        if rows == 0:
            return 0
        columns = len(board[0])

        count = 0

        for i in range(rows):
            for j in range(columns):
                if board[i][j] == '.':
                    continue
                if i > 0 and board[i - 1][j] == 'X':
                    continue
                if j > 0 and board[i][j - 1] == 'X':
                    continue

                count += 1

        return count
