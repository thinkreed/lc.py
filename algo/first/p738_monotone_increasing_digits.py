class Solution:
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        nums = [int(num) for num in str(N)]

        pivit = len(nums)
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                pivit = i
                nums[i - 1] = nums[i - 1] - 1

        for i in range(pivit, len(nums)):
            nums[i] = 9

        return int(''.join([str(d) for d in nums]))
