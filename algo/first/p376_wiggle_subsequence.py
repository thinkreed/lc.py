from itertools import groupby


class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        without_repeat = [num for num, _ in groupby(nums)]
        compares = zip(without_repeat, without_repeat[1:], without_repeat[2:])
        return sum((b > a) == (b > c) for a, b, c in compares) + len(without_repeat[:2])
