class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        dist = [float('inf')] * (N + 1)
        dist[K] = 0

        for i in range(N):
            for e in times:
                u = e[0]
                v = e[1]
                w = e[2]
                if dist[u] != float('inf') and dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w

        maxwait = 0
        for i in range(1, N + 1):
            maxwait = max(maxwait, dist[i])

        return -1 if maxwait == float('inf') else maxwait
