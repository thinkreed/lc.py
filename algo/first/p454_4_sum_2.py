from collections import Counter


class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        a_plus_b = Counter([a + b for a in A for b in B])

        result = 0

        for c in C:
            for d in D:
                result += a_plus_b.get(-c - d, 0)

        return result

    def four_sum_count(self, A, B, C, D):
        a_plus_b = Counter([a + b for a in A for b in B])
        return sum(a_plus_b[-c - d] for c in C for d in D)
