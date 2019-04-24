class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length = 0

        for i in range(len(nums)):
            current_length = 0
            j = i
            while nums[j] >= 0:
                num = nums[j]
                nums[j] = -1
                j = num
                current_length += 1

            max_length = max(current_length, max_length)

        return max_length
