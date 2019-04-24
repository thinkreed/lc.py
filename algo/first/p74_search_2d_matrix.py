class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])
        if m == 0:
            return False
        left = 0
        right = m * n - 1

        while left != right:
            mid = (left + right - 1) // 2
            if matrix[mid // m][mid % m] < target:
                left = mid + 1
            else:
                right = mid

        return matrix[right // m][right % m] == target
