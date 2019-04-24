class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix) < 1 or len(matrix[0]) < 1:
            return False
        row = 0
        column = len(matrix[0]) - 1
        while row < len(matrix) and column >= 0:
            if matrix[row][column] > target:
                column -= 1
            elif matrix[row][column] < target:
                row += 1
            else:
                return True

        return False
