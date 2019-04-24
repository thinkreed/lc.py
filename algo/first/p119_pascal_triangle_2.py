class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [[1]]

        for i in range(rowIndex + 1):
            result.append(list(map(lambda x, y: x + y, result[-1] + [0], [0] + result[-1])))

        return result[rowIndex]
