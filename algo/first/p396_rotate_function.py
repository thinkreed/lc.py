class Solution:
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        sumary = 0
        n = len(A)
        f = 0
        for i in range(n):
            f += i * A[i]
            sumary += A[i]

        res = f

        for i in range(n - 1, 0, -1):
            f = f + sumary - n * A[i]
            res = max(f, res)

        return res
