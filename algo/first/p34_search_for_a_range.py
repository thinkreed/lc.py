class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        i = 0
        j = len(nums) - 1

        res = [-1] * 2

        while i < j:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid

        if nums[i] != target:
            return res
        else:
            res[0] = i

        j = len(nums) - 1

        while i < j:
            mid = (i + j) // 2 + 1
            if nums[mid] > target:
                j = mid - 1
            else:
                i = mid

        res[1] = j

        return res
