class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = set()

        for i in range(9):
            for j in range(9):
                number = board[i][j]
                if number != '.':
                    row_code = str(number) + " in row " + str(i)
                    if row_code in seen:
                        return False

                    seen.add(row_code)

                    column_code = str(number) + " in column " + str(j)
                    if column_code in seen:
                        return False
                    seen.add(column_code)

                    block_code = str(number) + " in block " + str(i // 3) + "-" + str(j // 3)
                    if block_code in seen:
                        return False

                    seen.add(block_code)

        return True
