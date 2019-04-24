class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = -1
        max_left = None
        min_right = None
        left = 0
        right = len(nums) - 1
        while right >= 0:
            if not max_left or nums[left] > max_left:
                max_left = nums[left]

            if nums[left] != max_left:
                j = left

            if not min_right or nums[right] < min_right:
                min_right = nums[right]

            if nums[right] != min_right:
                i = right

            left += 1
            right -= 1

        return j - i + 1

a = [2,6,4,8,10,9,15]
print(Solution().findUnsortedSubarray(a))