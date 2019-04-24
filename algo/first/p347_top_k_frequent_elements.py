from collections import Counter
from itertools import chain


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        pairs = [[] for _ in nums]

        for num, count in Counter(nums).items():
            pairs[-count].append(num)

        return list(chain(*pairs))[:k]
