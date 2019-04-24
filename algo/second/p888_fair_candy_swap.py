class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        diff = (sum(A) - sum(B)) // 2
        set_a = set(A)
        set_b = set(B)

        for size in set_b:
            if diff + size in set_a:
                return [diff + size, size]

        return []
