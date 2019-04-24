class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        res = 0
        i = 0
        n = len(seats)

        for j in range(n):
            if seats[j] == 1:
                if i == 0:
                    res = max(res, j - i)
                else:
                    res = max(res, (j - i + 1) / 2)
                i = j + 1

        return max(res, n - i)
