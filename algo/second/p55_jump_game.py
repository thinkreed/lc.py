class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0

        for index, step in enumerate(nums):
            if index > max_reach:
                return False

            if index + step > max_reach:
                max_reach = index + step

        return True
