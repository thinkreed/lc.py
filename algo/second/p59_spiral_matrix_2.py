class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [([0] * n) for _ in range(n)]
        count = 1

        if n % 2 == 1:
            l = int((n + 1) / 2)
        else:
            l = int(n / 2)

        for i in range(l):
            for j in range(i, n):
                res[i][j] = count
                count += 1
            for k in range(i + 1, n):
                res[k][n - 1] = count
                count += 1
            for p in range(i + 1, n):
                res[n - 1][n - p - 1 + i] = count
                count += 1
            for q in range(i, n - 2):
                res[n - q - 2 + i][i] = count
                count += 1

            n -= 1

        return res
