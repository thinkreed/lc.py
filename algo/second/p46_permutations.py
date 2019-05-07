class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []

        def helper(index):
            if index == n:
                res.append(nums[:])

            for i in range(index, n):
                nums[index], nums[i] = nums[i], nums[index]
                helper(index + 1)
                nums[index], nums[i] = nums[i], nums[index]

        helper(0)

        return res
