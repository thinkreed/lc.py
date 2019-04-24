class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = {0: 1}
        sumary = 0
        ans = 0

        for num in nums:
            sumary += num
            ans += count.get(sumary - k, 0)
            count[sumary] = count.get(sumary, 0) + 1

        return ans
