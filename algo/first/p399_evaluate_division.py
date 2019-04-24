from collections import defaultdict
from itertools import permutations


class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        weights = defaultdict(dict)
        for (node1, node2), val in zip(equations, values):
            weights[node1][node1] = weights[node2][node2] = 1.0
            weights[node1][node2] = val
            weights[node2][node1] = 1 / val

        for k, i, j in permutations(weights, 3):
            if k in weights[i] and j in weights[k]:
                weights[i][j] = weights[i][k] * weights[k][j]

        return [weights[node1].get(node2, -1.0) for node1, node2 in queries]
