class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        def dfs(vertex, current_color):
            if vertex in colored:
                return colored[vertex] == current_color
            colored[vertex] = current_color
            return all(dfs(w, current_color ^ 1) for w in graph[vertex])

        colored = {}
        return all(dfs(vertex, 0) for vertex in range(len(graph)) if vertex not in colored)
