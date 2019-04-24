class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def helper(tmp, index):
            res.append(tmp)
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                helper(tmp + [nums[i]], i + 1)

        res = []
        nums = sorted(nums)
        helper([], 0)
        return res
