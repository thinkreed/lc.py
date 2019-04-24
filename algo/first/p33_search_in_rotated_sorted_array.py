class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)

        while low < high:
            mid = (low + high) / 2
            num = nums[mid] if (nums[mid] < nums[0]) == (target < nums[0]) else float('-inf') if target < nums[
                0] else float('inf')

            if num < target:
                low = mid + 1
            elif num > target:
                high = mid
            else:
                return mid

        return -1
