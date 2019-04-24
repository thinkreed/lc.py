class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if not matrix or len(matrix) == 0:
            return []

        m = len(matrix)
        n = len(matrix[0])

        row = 0
        column = 0
        step = 1

        result = [0] * (m * n)

        for i in range(m * n):
            result[i] = matrix[row][column]
            row -= step
            column += step

            if row >= m:
                row = m - 1
                column += 2
                step = -step

            if column >= n:
                column = n - 1
                row += 2
                step = -step

            if row < 0:
                row = 0
                step = -step

            if column < 0:
                column = 0
                step = -step

        return result
