class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def dfs(path, index, target):
            if index == n:
                if path[0] == target and path[1] == target and path[2] == target:
                    return True
                return False

            for i in range(4):
                if path[i] + nums[index] > target:
                    continue
                path[i] += nums[index]
                if dfs(path, index + 1, target):
                    return True
                path[i] -= nums[index]

            return False

        n = len(nums)
        if not nums or n < 4:
            return False
        sumary = sum(nums)
        if sumary % 4 != 0:
            return False

        nums.sort(reverse=True)

        return dfs([0] * 4, 0, sumary // 4)
