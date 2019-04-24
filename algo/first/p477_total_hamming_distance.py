class Solution:
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        n = len(nums)

        for i in range(32):
            current_bit_set_count = 0

            for num in nums:
                current_bit_set_count += (num >> i) & 1

            result += current_bit_set_count * (n - current_bit_set_count)

        return result
