class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """

        counter = {}

        for layer in wall:
            length = 0
            for brick in layer[:-1]:
                length += brick
                if length in counter:
                    counter[length] += 1
                else:
                    counter[length] = 1

        if not counter:
            return len(wall)

        return len(wall) - max(counter.values())
