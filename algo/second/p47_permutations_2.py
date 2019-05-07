class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        if not nums: return [[]]
        res = []
        for l in self.permuteUnique(nums[1:]):
            for ins in range((l + [nums[0]]).index(nums[0]) + 1):
                res.append(l[:ins] + [nums[0]] + l[ins:])
        return res
