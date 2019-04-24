class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = -1

        i_min = float("inf")
        j_max = float("-inf")

        left = 0
        right = len(nums) - 1

        while right >= 0:
            j_max = max(j_max, nums[left])
            if nums[left] != j_max:
                j = left

            i_min = min(i_min, nums[right])
            if nums[right] != i_min:
                i = right

            left += 1
            right -= 1

        return j - i + 1
