class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index_dict = {0: 0}
        count = 0
        max_len = 0

        for i in range(len(nums)):
            count += nums[i] or -1
            if count not in index_dict:
                index_dict[count] = i + 1
            else:
                max_len = max(max_len, i + 1 - index_dict[count])

        return max_len
