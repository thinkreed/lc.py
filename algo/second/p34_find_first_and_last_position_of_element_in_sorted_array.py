class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        n_len = len(nums)

        if n_len == 0:
            return [-1, -1]

        i = 0
        j = n_len - 1

        while i <= j:
            mid = (i + j) // 2

            if nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1

        end_index = j

        i, j = 0, n_len - 1

        while i <= j:
            mid = (i + j) // 2

            if nums[mid] >= target:
                j = mid - 1
            else:
                i = mid + 1

        start_index = i

        if start_index <= end_index:
            return [start_index, end_index]

        return [-1, -1]
