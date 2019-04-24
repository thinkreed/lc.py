class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cache = {}

        def helper(start, end):
            if (start, end) not in cache:
                cache[(start, end)] = nums[start] if start == end else \
                    max(nums[start] - helper(start + 1, end), nums[end] - helper(start, end - 1))
            return cache[(start, end)]

        return helper(0, len(nums) - 1) >= 0
