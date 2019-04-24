class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        current = float('-inf')
        count = 0

        for pair in sorted(pairs, key=lambda p: p[1]):
            if current < pair[0]:
                current = pair[1]
                count += 1

        return count
