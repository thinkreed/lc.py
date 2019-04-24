class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0

        i = 0
        n_len = len(nums)

        while i < n_len:
            tmp = 1

            while i + 1 < n_len and nums[i] < nums[i + 1]:
                tmp += 1
                i += 1

            res = max(res, tmp)
            i += 1

        return res
