class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0, 0]
        for i, num in enumerate(nums):
            val = abs(num)
            result[1] ^= (i + 1) ^ val
            if nums[val - 1] < 0:
                result[0] = val
            else:
                nums[val - 1] = -nums[val - 1]

        result[1] ^= result[0]
        return result
