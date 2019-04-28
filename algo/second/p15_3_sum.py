class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)

        n_len = len(nums)

        res = []

        for i in range(n_len - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                low = i + 1
                high = n_len - 1
                target = 0 - nums[i]

                while low < high:
                    if nums[low] + nums[high] < target:
                        low += 1
                    elif nums[low] + nums[high] > target:
                        high -= 1
                    else:
                        res.append((nums[i], nums[low], nums[high]))

                        while low < high and nums[low] == nums[low + 1]:
                            low += 1

                        while low < high and nums[high] == nums[high - 1]:
                            high -= 1

                        low += 1
                        high -= 1

        return res
