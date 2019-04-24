class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums, reverse=True)
        res = 0
        n = len(nums)

        for i in range(n):
            left = i + 1
            right = n - 1

            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    res += right - left
                    left += 1
                else:
                    right -= 1

        return res
