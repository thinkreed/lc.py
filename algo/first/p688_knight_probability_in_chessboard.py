class Solution:
    def __init__(self):
        self.mem = {}

    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        if (r, c, K) in self.mem:
            return self.mem[(r, c, K)]

        if r >= 2 * K and r + 2 * K < N and c >= 2 * K and c + 2 * K < N:
            return 1
        d = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

        ret = 0
        for (dr, dc) in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                ret += 0.125 * self.knightProbability(N, K - 1, nr, nc)

        self.mem[(r, c, K)] = ret
        self.mem[(c, r, K)] = ret
        self.mem[(N - 1 - r, N - 1 - c, K)] = ret
        self.mem[(N - 1 - c, N - 1 - r, K)] = ret
        return ret


print(Solution().knightProbability(3, 3, 0, 0))
# dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(K + 1)]
# moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, -1), (2, 1), (-2, -1), (-2, 1)]
#
# def helper(dp, N, k, r, c):
#     if r < 0 or r >= N or c < 0 or c >= N:
#         return 0.0
#
#     if k == 0:
#         return 1.0
#
#     if dp[k][r][c] != 0.0:
#         return dp[k][r][c]
#
#     for i in range(0, 8):
#         dp[k][r][c] += helper(dp, N, k - 1, r + moves[i][0], c + moves[i][1])
#
#     return dp[k][r][c]
#
# return helper(dp, N, K, r, c) / pow(8.0, K)
