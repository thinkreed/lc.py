class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)

        if s & 1 == 1:
            return False

        s //= 2

        dp = [False] * (s + 1)
        dp[0] = True

        for num in nums:
            for i in range(s, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[s]

    def can_partition(self, nums):
        s = 0
        bits = 1

        for num in nums:
            s += num
            bits |= bits << num

        return not (s & 1) and ((bits >> (s >> 1)) & 1) == 1
