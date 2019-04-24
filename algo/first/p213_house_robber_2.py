class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def helper(low, high):
            include = 0
            exclude = 0
            for j in range(low, high + 1):
                i = include
                e = exclude
                include = e + nums[j]
                exclude = max(e, i)
            return max(include, exclude)

        if len(nums) == 1:
            return nums[0]

        return max(helper(0, len(nums) - 2), helper(1, len(nums) - 1))
