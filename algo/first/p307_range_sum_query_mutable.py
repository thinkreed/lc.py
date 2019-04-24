class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.n = len(nums)
        self.dp = [0] * (self.n + 1)

        for i in range(self.n):
            k = i + 1
            while k <= self.n:
                self.dp[k] += nums[i]
                k += (k & -k)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self.nums[i]
        self.nums[i] = val
        i += 1
        while i <= self.n:
            self.dp[i] += diff
            i += (i & -i)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        res = 0
        j = j + 1
        while j:
            res += self.dp[j]
            j -= (j & -j)

        while i:
            res -= self.dp[i]
            i -= (i & -i)

        return res

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
