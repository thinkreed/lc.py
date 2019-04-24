class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        s1_len = len(s1)
        s2_len = len(s2)

        dp = [[0] * (s2_len + 1) for _ in range(s1_len + 1)]

        for j in range(1, s2_len + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        for i in range(1, s1_len + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])

            for j in range(1, s2_len + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))

        return dp[s1_len][s2_len]
