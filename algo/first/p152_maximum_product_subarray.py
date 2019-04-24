class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]

        tmpMax = res
        tmpMin = res

        for i in range(1, len(nums)):
            if nums[i] < 0:
                tmpMax, tmpMin = tmpMin, tmpMax

            tmpMax = max(nums[i], tmpMax * nums[i])
            tmpMin = min(nums[i], tmpMin * nums[i])

            res = max(res, tmpMax)

        return res
