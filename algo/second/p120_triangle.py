class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        min_len = triangle[-1]

        for layer in range(n - 2, -1, -1):
            for i in range(layer + 1):
                min_len[i] = min(min_len[i], min_len[i + 1] + triangle[layer][i])

        return min_len[0]
