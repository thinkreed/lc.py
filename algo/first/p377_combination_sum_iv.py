class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def helper(nums, target):
            if dp[target] != -1:
                return dp[target]

            res = 0
            for num in nums:
                if target >= num:
                    res += helper(nums, target - num)
            dp[target] = res
            return res

        dp = [-1] * (target + 1)
        dp[0] = 1

        return helper(nums, target)

    def combination_sum4(self, nums, target):
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1

        for i in range(1, len(dp)):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]

        return dp[target]
