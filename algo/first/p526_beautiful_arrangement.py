cache = {}


class Solution(object):

    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        return self.helper(N, tuple(range(1, N + 1)))

    def helper(self, num, positions):
        if num == 1:
            return 1

        key = (num, positions)

        if key in cache:
            return cache[key]

        count = 0

        for j in range(len(positions)):
            if positions[j] % num == 0 or num % positions[j] == 0:
                count += self.helper(num - 1, positions[:j] + positions[j + 1:])

        cache[key] = count
        return count
