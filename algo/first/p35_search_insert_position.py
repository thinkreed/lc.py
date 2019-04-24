class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        for i, num in enumerate(nums):
            if target <= num:
                return i
        return len(nums)

    def searchInsertBinary(self, nums, target):
        i, j = 0, len(nums) - 1
        while i <= j:
            mid_index = (i + j) // 2
            mid_value = nums[mid_index]
            if target < mid_value:
                j = mid_index - 1
            elif target > mid_value:
                i = mid_index + 1
            else:
                return mid_index
        return i
