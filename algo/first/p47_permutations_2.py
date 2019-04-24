class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(path):
            if len(path) == n:
                res.append(list(path))
                return
            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and nums[i - 1] == nums[i] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(nums[i])
                dfs(path)
                used[i] = False
                path.pop()

        res = []
        n = len(nums)
        if not nums or n == 0:
            return res

        used = [False] * n
        nums = sorted(nums)
        dfs([])
        return res
