class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 2:
            return True

        small = False
        big = False

        for i in range(1, len(A)):
            if A[i - 1] > A[i]:
                big = True

            if A[i - 1] < A[i]:
                small = True

            if small and big:
                return False

        return True
