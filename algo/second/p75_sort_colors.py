class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        red_index = 0
        white_index = 0
        n = len(nums)

        for blue_index in range(n):
            color = nums[blue_index]
            nums[blue_index] = 2

            if color < 2:
                nums[white_index] = 1
                white_index += 1

            if color == 0:
                nums[red_index] = 0
                red_index += 1
