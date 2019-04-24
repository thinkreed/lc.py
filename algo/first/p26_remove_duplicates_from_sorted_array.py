class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1 if len(nums) > 0 else 0
        for index, num in enumerate(nums):
            if num > nums[i - 1]:
                nums[i] = num
                i += 1
        return i
