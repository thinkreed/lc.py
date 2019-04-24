class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count_of_one = 0
        while n | 0 != 0:
            count_of_one += n & 1
            n = n >> 1

        return count_of_one

    def hamming_weight_2(self, n):
        count = 0
        while n != 0:
            n = n & (n - 1)
            count += 1
        return count
