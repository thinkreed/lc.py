from collections import Counter


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0

        c = Counter(nums)

        for num in c:
            if k > 0 and num + k in c or k == 0 and c[num] > 1:
                res += 1

        return res
