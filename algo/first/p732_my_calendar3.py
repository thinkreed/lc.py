class MyCalendarThree(object):

    def __init__(self):
        self.ss, self.es = [], []
        self.k = 0

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        from bisect import bisect_left as bl, bisect_right as br, insort_left as il
        from heapq import heappop, heappush
        i, j = bl(self.es, start), br(self.ss, end)
        il(self.ss, start, i, j)
        il(self.es, end, i, j)
        heap = []
        for pp in range(i, j + 1):
            while heap and heap[0] <= self.ss[pp]:
                heappop(heap)
            heappush(heap, self.es[pp])
            self.k = max(self.k, len(heap))
        return self.k

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
