class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]

        last = self.subsets(nums[:-1])

        return last + [subset + [nums[-1]] for subset in last]
