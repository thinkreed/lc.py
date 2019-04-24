class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        l = 0
        r = n - 1

        while l + 1 < n and A[l] < A[l + 1]:
            l += 1

        while r > 0 and A[r] < A[r - 1]:
            r -= 1

        return 0 < l == r < n - 1
