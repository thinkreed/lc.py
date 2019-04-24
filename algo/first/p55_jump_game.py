class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        n = len(nums)
        reach = 0

        while i < n and i <= reach:
            reach = max(i + nums[i], reach)
            i += 1

        return i == n
