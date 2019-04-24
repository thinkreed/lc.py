class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """

        def count_subsets_equal_to_target(nums, target):
            dp = [0] * (target + 1)
            dp[0] = 1

            for num in nums:
                for i in range(target, num - 1, -1):
                    dp[i] += dp[i - num]

            return dp[target]

        sumary = sum(nums)

        return 0 if sumary < S or (sumary + S) % 2 > 0 else count_subsets_equal_to_target(nums, (sumary + S) >> 1)
