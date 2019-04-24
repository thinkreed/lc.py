from itertools import chain
from itertools import islice


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c != len(nums) * len(nums[0]):
            return nums

        chained = chain(*nums)

        return [list(islice(chained, c)) for _ in xrange(r)]
