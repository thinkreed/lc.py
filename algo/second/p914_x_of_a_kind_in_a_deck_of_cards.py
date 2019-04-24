from fractions import gcd
from collections import Counter


class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        return reduce(gcd, Counter(deck).values()) > 1
