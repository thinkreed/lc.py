class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        difference = x ^ y
        count = 0
        while difference:
            if difference & 1 == 1:
                count += 1
            difference = difference >> 1
        return count

    def hamming_distance(self, x, y):
        return bin(x ^ y).count('1')
