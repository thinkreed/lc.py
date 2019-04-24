class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def permute_backtracking(result, temp_list, nums):
            if len(temp_list) == len(nums):
                result.append(list(temp_list))
            else:
                for num in nums:
                    if num in temp_list:
                        continue

                    temp_list.append(num)
                    permute_backtracking(result, temp_list, nums)
                    temp_list.pop()

        res = []
        permute_backtracking(res, [], nums)
        return res
