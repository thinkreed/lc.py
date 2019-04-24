class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0:
            return False
        n = len(nums)
        dict = {}
        width = t + 1
        for i in xrange(n):
            m = nums[i] / width
            if m in dict:
                return True
            if m - 1 in dict and abs(nums[i] - dict[m - 1]) < width:
                return True
            if m + 1 in dict and abs(nums[i] - dict[m + 1]) < width:
                return True
            dict[m] = nums[i]
            if i >= k:
                del dict[nums[i - k] / width]
        return False
