class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b0 = 0
        b1 = 0

        for num in nums:
            b0 = (b0 ^ num) & ~b1
            b1 = (b1 ^ num) & ~b0

        return b0
