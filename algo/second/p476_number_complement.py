class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        mask = ~0

        while num & mask:
            mask <<= 1

        return ~num & ~mask
