class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []

        if not matrix:
            return []

        row_len = len(matrix)
        col_len = len(matrix[0])

        s_row = 0
        s_col = 0
        e_row = row_len - 1
        e_col = col_len - 1

        if s_row == e_row or s_col == e_col:
            return [matrix[i][j] for i in range(row_len) for j in range(col_len)]

        while s_col <= e_col and s_row <= e_row:
            for i in range(s_col, e_col + 1):
                res.append(matrix[s_row][i])

            s_row += 1

            for j in range(s_row, e_row + 1):
                res.append(matrix[j][e_col])

            e_col -= 1

            if s_row <= e_row:
                for m in range(e_col, s_col - 1, -1):
                    res.append(matrix[e_row][m])

            e_row -= 1

            if s_col <= e_col:
                for n in range(e_row, s_row - 1, -1):
                    res.append(matrix[n][s_col])

            s_col += 1

        return res
