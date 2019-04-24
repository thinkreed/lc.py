class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a_xor_b = 0
        a = 0
        b = 0

        for num in nums:
            a_xor_b ^= num

        different = a_xor_b & (-a_xor_b)

        for num in nums:
            if num & different == 0:
                a ^= num
            else:
                b ^= num

        return a, b
