class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i, j = 0, len(nums) - 1
        count = 0
        while i < j:
            count += nums[j] - nums[i]
            i += 1
            j -= 1

        return count
