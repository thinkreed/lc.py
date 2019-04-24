import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.pq = nums
        self.size = k

        heapq.heapify(self.pq)

        while len(self.pq) > k:
            heapq.heappop(self.pq)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.pq) < self.size:
            heapq.heappush(self.pq, val)
        else:
            heapq.heappushpop(self.pq, val)

        return self.pq[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
