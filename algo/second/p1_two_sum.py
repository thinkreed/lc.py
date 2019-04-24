class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        c = {}

        for index, num in enumerate(nums):
            if target - num in c:
                return [index, c[target - num]]
            else:
                c[num] = index

        return []
