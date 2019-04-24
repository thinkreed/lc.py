class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = 0
        maximum = 0

        for i, num in enumerate(arr):
            maximum = max(maximum, num)

            if maximum == i:
                count += 1

        return count
