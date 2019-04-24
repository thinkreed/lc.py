from collections import defaultdict
import heapq


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = defaultdict(dict)
        for fro, to, price in flights:
            prices[fro][to] = price
        heap = [(0, src, k + 1)]
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in prices[i]:
                    heapq.heappush(heap, (p + prices[i][j], j, k - 1))
        return -1
