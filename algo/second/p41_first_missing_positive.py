class Solution(object):
    def firstMissingPositive(self, nums):
        n_len = len(nums)
        for i in xrange(n_len):
            while 0 <= nums[i] - 1 < n_len and nums[nums[i] - 1] != nums[i]:
                tmp = nums[i] - 1
                nums[i], nums[tmp] = nums[tmp], nums[i]
        for i in xrange(n_len):
            if nums[i] != i + 1:
                return i + 1
        return n_len + 1
