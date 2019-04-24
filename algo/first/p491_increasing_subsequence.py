class Solution:
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def helper(tmp, index):
            if len(tmp) > 1:
                res.append(list(tmp))

            counted = set()

            for i in range(index, len(nums)):
                if nums[i] in counted:
                    continue

                if len(tmp) == 0 or nums[i] >= tmp[-1]:
                    counted.add(nums[i])
                    tmp.append(nums[i])
                    helper(tmp, i + 1)
                    del tmp[-1]

        helper([], 0)
        return res
