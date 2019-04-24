class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 0:
            return 0
        points = sorted(points, key=lambda point: point[1])
        count = 1
        end_position = points[0][1]
        for i in range(1, len(points)):
            if end_position >= points[i][0]:
                continue

            count += 1
            end_position = points[i][1]

        return count
