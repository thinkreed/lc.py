class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return [[]]

        dp = {0: [[]], 1: [[s[0]]]}
        s_len = len(s)

        for i in range(1, s_len):
            dp[i + 1] = []

            for j in range(0, i + 1):
                tmp = s[j:i + 1]
                if tmp == tmp[::-1]:
                    for sol in dp[j]:
                        dp[i + 1].append(sol + [tmp])

        return dp[s_len]
