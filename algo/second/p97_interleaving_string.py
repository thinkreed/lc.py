class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m = len(s1)
        n = len(s2)
        o = len(s3)

        if m + n != o:
            return False

        def dfs(i, j, k, invalid):
            if invalid[i][j]:
                return False

            if k == o:
                return True

            valid = (i < m and s1[i] == s3[k] and dfs(i + 1, j, k + 1, invalid)) or (
                    j < n and s2[j] == s3[k] and dfs(i, j + 1, k + 1, invalid))

            if not valid:
                invalid[i][j] = True

            return valid

        return dfs(0, 0, 0, [[0 for _ in range(n + 1)] for _ in range(m + 1)])
