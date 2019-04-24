class Solution:
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        def dfs(current, n):
            res.append(current)
            i = current * 10
            while i <= n and i < current * 10 + 10:
                dfs(i, n)
                i += 1

        res = []
        j = 1
        while j < 10 and j <= n:
            dfs(j, n)
            j += 1

        return res


print(Solution().lexicalOrder(500))
