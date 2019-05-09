class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = []

        def dfs(cur, invalid_diff, invalid_sum):
            i = len(cur)

            if i == n:
                res.append(cur)
                return

            for j in range(n):
                if j not in cur and i - j not in invalid_diff and i + j not in invalid_sum:
                    dfs(cur + [j], invalid_diff + [i - j], invalid_sum + [i + j])

        dfs([], [], [])
        return len(res)
