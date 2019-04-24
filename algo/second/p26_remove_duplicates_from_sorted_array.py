class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1 if len(nums) > 0 else 0

        for num in nums:
            if num > nums[i - 1]:
                nums[i] = num
                i += 1

        return i
