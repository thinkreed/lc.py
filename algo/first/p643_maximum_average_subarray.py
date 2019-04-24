class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sumary = 0

        for i in range(k):
            sumary += nums[i]

        current_max = sumary

        for i in range(k, len(nums)):
            sumary += nums[i] - nums[i - k]
            current_max = max(sumary, current_max)

        return current_max / k
