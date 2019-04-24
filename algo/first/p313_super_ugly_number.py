class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        res = [0] * n
        res[0] = 1
        cur = [0] * len(primes)

        for i in range(1, n):
            res[i] = float('inf')
            for j in range(len(primes)):
                if primes[j] * res[cur[j]] == res[i - 1]:
                    cur[j] += 1
                res[i] = min(res[i], primes[j] * res[cur[j]])

        return res[-1]
