class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        cur_start = 0
        cur_end = 0
        res = 0

        while cur_end < n - 1:
            res += 1
            max_end = cur_end + 1

            for i in range(cur_start, cur_end + 1):
                if i + nums[i] >= n - 1:
                    return res

                max_end = max(max_end, i + nums[i])
            cur_start, cur_end = cur_end + 1, max_end

        return res
