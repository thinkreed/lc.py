from collections import Counter


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = Counter(nums)
        res = 0

        for num in counts:
            if num + 1 in counts:
                res = max(res, counts[num] + counts[num + 1])

        return res
