class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        previous_robbed = 0
        previous_not_robbed = 0
        for num in nums:
            rob_current = previous_not_robbed + num
            not_rob_current = max(previous_not_robbed, previous_robbed)

            previous_not_robbed = not_rob_current
            previous_robbed = rob_current

        return max(previous_not_robbed, previous_robbed)
