class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0

        for i in range(32)[::-1]:
            result <<= 1
            prefixes = {n >> i for n in nums}
            result += any(result ^ 1 ^ prefix in prefixes for prefix in prefixes)
        return result
