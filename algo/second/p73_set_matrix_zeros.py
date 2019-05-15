class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        zero_row = False
        zero_col = False

        for i in range(m):
            if matrix[i][0] == 0:
                zero_col = True
                break

        for i in range(n):
            if matrix[0][i] == 0:
                zero_row = True
                break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if zero_col:
            for i in range(m):
                matrix[i][0] = 0

        if zero_row:
            for j in range(n):
                matrix[0][j] = 0
