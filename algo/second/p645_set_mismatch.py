class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s_set = sum(set(nums))
        s_num = sum(nums)
        s_range = sum(range(1, len(nums) + 1))

        return [s_num - s_set, s_range - s_set]
