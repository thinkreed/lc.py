class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        mid = 0

        while low < high:
            mid = low + (high - low) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] < nums[high]:
                high = mid
            else:
                high -= 1

        return nums[low]
