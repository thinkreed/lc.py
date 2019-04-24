class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        prime_list = [True] * n
        i = 2
        count = 0
        while i < n:
            if prime_list[i]:
                count += 1
                j = 2
                while j * i < n:
                    prime_list[j * i] = False
                    j += 1
            i += 1

        return count
