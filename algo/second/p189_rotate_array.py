class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        def reverseHelper(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        n_len = len(nums)

        k = k % n_len

        reverseHelper(0, n_len - 1)
        reverseHelper(0, k - 1)
        reverseHelper(k, n_len - 1)
