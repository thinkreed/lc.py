class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        tmp = res = sum(nums[:k])
        n_len = len(nums)

        for i in range(k, n_len):
            tmp = tmp + nums[i] - nums[i - k]

            if tmp > res:
                res = tmp

        return res / float(k)
