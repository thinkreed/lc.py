class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        minlen = triangle[-1]

        for layer in range(n - 2, -1, -1):
            for i in range(layer + 1):
                minlen[i] = min(minlen[i], minlen[i + 1]) + triangle[layer][i]

        return minlen[0]
