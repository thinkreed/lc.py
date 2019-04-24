class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        s = []
        for num in arr:
            cur_max = num if len(s) == 0 else max(s[-1], num)
            while s and s[-1] > num:
                s.pop()

            s.append(cur_max)

        return len(s)
