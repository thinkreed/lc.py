class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return True

            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1

            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False
