class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)

        if s_len <= 1:
            return 0

        dp = [0 for _ in range(s_len)]

        res = 0

        for i in range(1, s_len):
            if s[i] == ')' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                dp[i] = dp[i - 1] + 2 + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] - 2 > 0 else 0)
                res = max(res, dp[i])

        return res
