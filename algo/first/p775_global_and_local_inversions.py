class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        for index, num in enumerate(A):
            if abs(num - index) > 1:
                return False

        return True
