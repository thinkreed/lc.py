class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        n = len(intervals)

        if n <= 1:
            return intervals

        intervals = sorted(intervals, key=lambda val: val[0])

        res = [intervals[0]]

        for i in range(1, n):
            if res[-1][1] >= intervals[i][1]:
                continue
            elif res[-1][1] >= intervals[i][0]:
                res[-1][1] = intervals[i][1]
            else:
                res.append(intervals[i])

        return res
