class Solution:
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        cache = {}

        def collect(n, k):
            if (n, k) in cache:
                return cache[n, k]

            if n < k:
                return 0

            if k == 1:
                cache[n, k] = sum(A[:n]) / n
                return cache[n, k]

            current = 0
            cache[n, k] = 0
            for i in range(n - 1, 0, -1):
                current += A[i]
                cache[n, k] = max(cache[n, k], collect(i, k - 1) + current / (n - i))
            return cache[n, k]

        return collect(len(A), K)
