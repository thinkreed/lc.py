# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        end = float('-inf')
        count = 0

        for i in sorted(intervals, key=lambda i: i.end):
            if i.start >= end:
                end = i.end

            else:
                count += 1

        return count
