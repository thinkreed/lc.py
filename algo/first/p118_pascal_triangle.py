class Solution(object):
    def generate(self, numRows):
        """

        current row can be constructed by using the offset sum of previous row
         110
        +011
         121
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1]]

        for i in range(numRows):
            result.append(list(map(lambda x, y: x + y, result[-1] + [0], [0] + result[-1])))

        return result[:numRows]