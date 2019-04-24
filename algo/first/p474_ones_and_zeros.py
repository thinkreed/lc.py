class Solution:
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for str in strs:
            zero_count = str.count('0')
            one_count = str.count('1')
            for i in range(m, zero_count - 1, -1):
                for j in range(n, one_count - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zero_count][j - one_count] + 1)

        return dp[m][n]

    def find_max_form(self, strs, m, n):
        def get_max(counts, m, n):
            res = 0
            for zeros, ones in counts:
                if m >= zeros and n >= ones:
                    res += 1
                    m -= zeros
                    n -= ones

            return res

        pairs = [(s.count('0'), s.count('1')) for s in strs]
        pair1 = sorted(pairs, key=lambda pair: -min(m - pair[0], n - pair[1]))
        pair2 = sorted(pairs, key=lambda pair: min(pair[0], pair[1]))
        return max(get_max(pair1, m, n), get_max(pair2, m, n))
