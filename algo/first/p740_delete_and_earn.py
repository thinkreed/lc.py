from collections import Counter


class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slots = Counter(nums)
        rob_previous = 0
        rob_current = 0
        last = None
        for val in sorted(slots):
            max_last = max(rob_previous, rob_current)

            if val - 1 != last:
                rob_current = val * slots[val] + max_last
                rob_previous = max_last
            else:
                rob_current = val * slots[val] + rob_previous
                rob_previous = max_last

            last = val

        return max(rob_previous, rob_current)
