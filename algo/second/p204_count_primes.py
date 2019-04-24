import math


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 2:
            return 0

        not_primes = [True] * n

        n_sqrt = int(round(n ** 0.5))

        not_primes[0] = False
        not_primes[1] = False

        for i in range(2, n_sqrt + 1):
            if not_primes[i]:

                j = 2

                while i * j < n:
                    v = i * j
                    not_primes[v] = False
                    j += 1

        return not_primes.count(True)
