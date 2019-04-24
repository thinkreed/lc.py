class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red_index = 0
        white_index = 0

        for blue_index in range(len(nums)):
            color = nums[blue_index]
            nums[blue_index] = 2

            if color < 2:
                nums[white_index] = 1
                white_index += 1

            if color == 0:
                nums[red_index] = 0
                red_index += 1
