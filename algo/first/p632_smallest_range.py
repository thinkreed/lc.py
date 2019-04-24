import heapq


class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        q = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(q)

        res = -1e9, 1e9

        max_val = max(row[0] for row in nums)

        while q:
            min_val, i, j = heapq.heappop(q)
            if max_val - min_val < res[1] - res[0]:
                res = min_val, max_val
            if j + 1 == len(nums[i]):
                return res

            x = nums[i][j + 1]
            max_val = max(max_val, x)
            heapq.heappush(q, (x, i, j + 1))
