class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]

        return max(nums)
