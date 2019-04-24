class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 1
        end = len(nums) - 1

        while start < end:
            middle = start + (end - start) // 2

            count = 0

            for num in nums:
                if num <= middle:
                    count += 1

            if count <= middle:
                start = middle + 1
            else:
                end = middle

        return start
