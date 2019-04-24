class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_of_nums = 0
        sum_of_left = 0
        for num in nums:
            sum_of_nums += num

        for i, num in enumerate(nums):
            if i != 0:
                sum_of_left += nums[i - 1]
            if (sum_of_nums - num - sum_of_left) == sum_of_left:
                return i

        return -1
