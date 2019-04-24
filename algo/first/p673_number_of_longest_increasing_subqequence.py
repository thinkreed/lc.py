class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = 0
        max_len = 0

        lens = [0] * n
        counts = [0] * n

        for i in range(n):
            lens[i] = counts[i] = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    if lens[i] == lens[j] + 1:
                        counts[i] += counts[j]

                    if lens[i] < lens[j] + 1:
                        lens[i] = lens[j] + 1
                        counts[i] = counts[j]

            if max_len == lens[i]:
                res += counts[i]

            if max_len < lens[i]:
                max_len = lens[i]
                res = counts[i]

        return res
