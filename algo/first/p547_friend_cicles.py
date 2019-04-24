class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        involved = set()

        def dfs(person):
            for other, friendship in enumerate(M[person]):
                if friendship and other not in involved:
                    involved.add(other)
                    dfs(other)

        result = 0

        for i in range(len(M)):
            if i not in involved:
                dfs(i)
                result += 1
        return result
