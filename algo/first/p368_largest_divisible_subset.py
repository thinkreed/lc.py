class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = {-1: set()}

        for num in sorted(nums):
            s[num] = max((s[d] for d in s if num % d == 0), key=len) | {num}

        return list(max(s.values(), key=len))

    def largest_divisible_subset(self, nums):
        nums = sorted(nums)
        temp = [0] * len(nums)
        parent = [0] * len(nums)

        m = 0
        mi = 0

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                if nums[j] % nums[i] == 0 and temp[i] < temp[j] + 1:
                    temp[i] = temp[j] + 1
                    parent[i] = j
                    if temp[i] > m:
                        m = temp[i]
                        mi = i

        res = []
        for i in range(m):
            res.append(nums[mi])
            mi = parent[mi]

        return res
