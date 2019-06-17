class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        b = 0

        for num in nums:
            a = (a ^ num) & ~b
            b = (b ^ num) & ~a

        return a
