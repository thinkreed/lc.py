class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        def binary_search(low, high, target):
            while low <= high:
                mid = (low + high) / 2
                if sums[mid] >= target:
                    high = mid - 1
                else:
                    low = mid + 1
            return low

        sums = [0] * (len(nums) + 1)

        for i in range(1, len(sums)):
            sums[i] = sums[i - 1] + nums[i - 1]

        res = float('inf')

        for i in range(len(sums)):
            end = binary_search(i + 1, len(sums) - 1, sums[i] + s)
            if end == len(sums):
                break

            if end - i < res:
                res = end - i

        return res if res != float('inf') else 0
