class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]

        n = len(nums)
        res = []

        nums = sorted(nums)

        def back_track(res, subset, cur):
            res.append(subset)

            if cur == n:
                return

            while cur < n:
                back_track(res, subset + [nums[cur]], cur + 1)

                while cur + 1 < n and nums[cur + 1] == nums[cur]:
                    cur += 1

                cur += 1

        back_track(res, [], 0)
        return res
