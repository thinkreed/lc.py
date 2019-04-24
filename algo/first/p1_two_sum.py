class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        passed_dict = {}

        for index, num in enumerate(nums):
            if num in passed_dict:
                return [passed_dict[num], index]
            else:
                passed_dict[target - num] = index
