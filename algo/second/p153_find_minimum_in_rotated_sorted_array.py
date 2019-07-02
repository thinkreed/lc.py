class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        start, end = 0, len(nums) - 1

        target = nums[-1]

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                end = mid
            else:
                start = mid

        if nums[start] < target:
            return nums[start]
        else:
            return nums[end]
