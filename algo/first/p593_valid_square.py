from itertools import combinations


class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """

        def distance(pair):
            return (pair[0][0] - pair[1][0]) ** 2 + (pair[0][1] - pair[1][1]) ** 2

        distances = set(map(distance, combinations((p1, p2, p3, p4), 2)))
        return len(distances) == 2 and 0 not in distances
