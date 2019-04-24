class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        position = 0

        for index, num in enumerate(nums):
            if num != 0:
                nums[position], nums[index] = nums[index], nums[position]
                position += 1
