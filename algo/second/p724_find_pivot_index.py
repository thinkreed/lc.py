class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_left = 0
        sum_right = sum(nums)

        for i, num in enumerate(nums):
            sum_right -= num

            if sum_right == sum_left:
                return i

            sum_left += num

        return -1
