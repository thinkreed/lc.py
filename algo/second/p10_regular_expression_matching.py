class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_len = len(s)
        p_len = len(p)

        dp = [[False] * (s_len + 1) for _ in range(p_len + 1)]
        dp[0][0] = True

        for i in range(1, p_len):
            dp[i + 1][0] = dp[i - 1][0] and p[i] == '*'

        for i in range(p_len):
            for j in range(s_len):
                if p[i] == '*':
                    if p[i - 1] != s[j] and p[i - 1] != '.':
                        dp[i + 1][j + 1] = dp[i - 1][j + 1]
                    else:
                        dp[i + 1][j + 1] = dp[i][j + 1] or dp[i - 1][j + 1] or dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i][j] and (p[i] == s[j] or p[i] == '.')

        return dp[-1][-1]
