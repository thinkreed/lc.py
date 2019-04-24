class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])

            return parent[x]

        parent = [0] * (len(edges) + 1)

        for i in range(len(parent)):
            parent[i] = i

        for u, v in edges:
            if find(parent, u) == find(parent, v):
                return [u, v]
            else:
                parent[find(parent, u)] = find(parent, v)

        return [0, 0]
