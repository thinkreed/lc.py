class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = []
        res = []

        f = [0] * n

        f[0] = 1

        for i in range(1, n):
            nums.append(i)
            f[i] = f[i - 1] * i

        nums.append(n)

        k -= 1

        for i in range(n, 0, -1):
            index = k // f[i - 1]
            k = k % f[i - 1]
            res.append(str(nums[index]))
            nums.pop(index)

        return ''.join(res)
