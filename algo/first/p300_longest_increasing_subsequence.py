class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = [0] * len(nums)
        res = 0

        for num in nums:
            i = 0
            j = res

            while i != j:
                middle = (i + j) // 2
                if tails[middle] < num:
                    i = middle + 1
                else:
                    j = middle

            tails[i] = num
            res = max(res, i + 1)

        return res
