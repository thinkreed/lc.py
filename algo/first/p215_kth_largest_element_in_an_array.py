import random


class Solution:

    def findKthLargest(self, nums, k):
        random.shuffle(nums)
        return self.find_kth_smallest(nums, len(nums) + 1 - k)

    def find_kth_smallest(self, nums, k):
        if nums:
            pos = self.partition(nums, 0, len(nums) - 1)
            if k > pos + 1:
                return self.find_kth_smallest(nums[pos + 1:], k - pos - 1)
            elif k < pos + 1:
                return self.find_kth_smallest(nums[:pos], k)
            else:
                return nums[pos]

    def partition(self, nums, l, r):
        index = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[index] = nums[index], nums[l]
                index += 1
            l += 1
        nums[index], nums[r] = nums[r], nums[index]
        return index
