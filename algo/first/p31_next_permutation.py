class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1
        k = n

        while n > 0 and nums[n - 1] >= nums[n]:
            n -= 1

        j = n

        while j < k:
            nums[j], nums[k] = nums[k], nums[j]
            j += 1
            k -= 1

        if n > 0:
            k = n
            n -= 1

            while nums[k] <= nums[n]:
                k += 1

            nums[n], nums[k] = nums[k], nums[n]
