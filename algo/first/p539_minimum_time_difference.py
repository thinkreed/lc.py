class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """

        def get_minutes(time_point):
            hour, minute = map(int, time_point.split(':'))
            return 60 * hour + minute

        minutes = sorted(map(get_minutes, timePoints))
        minutes.append(60 * 24 + minutes[0])
        return min(y - x for x, y in zip(minutes, minutes[1:]))
