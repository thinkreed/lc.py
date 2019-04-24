class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        self.dict = {}
        return self.dfs(range(1, maxChoosableInteger + 1), desiredTotal)

    def dfs(self, nums, desiredTotal):

        key = str(nums)
        if key in self.dict:
            return self.dict[key]

        if nums[-1] >= desiredTotal:
            return True

        for i in range(len(nums)):
            if not self.dfs(nums[:i] + nums[i + 1:], desiredTotal - nums[i]):
                self.dict[key] = True
                return True
        self.dict[key] = False
        return False
