class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        a = 0
        b = 0

        for num in nums:
            a, b = max(b + num, a), a

        return a
