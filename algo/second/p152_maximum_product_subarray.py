class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i_max = i_min = res = nums[0]

        for n in nums[1:]:
            i_max, i_min = max(n, n * i_max, n * i_min), min(n, n * i_max, n * i_min)
            res = max(res, i_max)

        return res
