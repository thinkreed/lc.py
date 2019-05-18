class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return [[]]

        return [sub + [i] for i in range(k, n + 1) for sub in self.combine(i - 1, k - 1)]
