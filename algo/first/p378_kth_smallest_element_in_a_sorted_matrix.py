class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        low = matrix[0][0]
        high = matrix[-1][-1]

        while low < high:
            middle = low + (high - low) // 2
            count = 0
            j = len(matrix[0]) - 1

            for i in range(len(matrix)):
                while j >= 0 and matrix[i][j] > middle:
                    j -= 1

                count += j + 1

            if count < k:
                low = middle + 1
            else:
                high = middle

        return low
