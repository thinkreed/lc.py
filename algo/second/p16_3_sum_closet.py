class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)

        res = nums[0] + nums[1] + nums[2]

        n_len = len(nums)

        for i in range(n_len - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                low = i + 1
                high = n_len - 1

                while low < high:
                    cur = nums[i] + nums[low] + nums[high]

                    if target == cur:
                        return cur

                    if abs(cur - target) < abs(res - target):
                        res = cur

                    if cur < target:
                        low += 1

                    elif cur > target:
                        high -= 1

        return res
