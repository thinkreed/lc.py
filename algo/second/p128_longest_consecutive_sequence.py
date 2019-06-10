class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in nums:
                tmp = num + 1

                while tmp in nums:
                    tmp += 1

                res = max(res, tmp - num)

        return res
