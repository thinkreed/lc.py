class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [[10000 * x for x in row] for row in matrix]
        for _ in range(4):
            for row in res:
                for j in range(1, len(row)):
                    row[j] = min(row[j], row[j - 1] + 1)
            res = map(list, zip(*res[::-1]))

        return res
