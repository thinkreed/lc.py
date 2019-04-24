class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        sort_num = sorted(nums)

        n = len(nums) - 1
        j = 0
        k = n / 2 + 1
        for i in range(n, -1, -1):
            if i & 1:
                nums[i] = sort_num[k]
                k += 1
            else:
                nums[i] = sort_num[j]
                j += 1
