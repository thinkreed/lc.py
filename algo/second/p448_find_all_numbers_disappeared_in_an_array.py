class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for x in range(n):
            i = abs(nums[x]) - 1
            nums[i] = -abs(nums[i])

        return [x + 1 for x in range(n) if nums[x] > 0]
