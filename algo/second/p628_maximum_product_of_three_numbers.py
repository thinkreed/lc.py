class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        x = nums[-1] * nums[-2] * nums[-3]
        y = nums[0] * nums[1] * nums[-1]

        return max(x, y)
