class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        p = 1
        i = 0
        j = 0
        total = 0

        while j < n:
            p *= nums[j]

            while i <= j and p >= k:
                p //= nums[i]
                i += 1

            total += (j - i + 1)
            j += 1

        return total
