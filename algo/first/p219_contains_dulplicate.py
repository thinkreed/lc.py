class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sliding_window = set()

        for i, num in enumerate(nums):
            if i > k:
                sliding_window.remove(nums[i - k - 1])

            if num in sliding_window:
                return True
            else:
                sliding_window.add(num)

        return False
