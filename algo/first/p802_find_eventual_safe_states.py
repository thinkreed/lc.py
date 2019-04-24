class Solution:
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """

        def dfs(index):
            if colors[index] != 0:
                return colors[index] == 1
            colors[index] = 2
            for node in graph[index]:
                if not dfs(node):
                    return False
            colors[index] = 1
            return True

        res = []
        if not graph or len(graph) == 0:
            return res

        count = len(graph)
        colors = [0] * count

        for i in range(count):
            if dfs(i):
                res.append(i)

        return res
