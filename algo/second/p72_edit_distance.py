class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)

        cost = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            cost[i][0] = i

        for i in range(1, n + 1):
            cost[0][i] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    cost[i][j] = cost[i - 1][j - 1]
                else:
                    cost[i][j] = min(cost[i - 1][j - 1], cost[i - 1][j], cost[i][j - 1]) + 1

        return cost[m][n]
