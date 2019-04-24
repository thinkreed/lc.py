class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        def concatenate(k, n, capcity):
            if not k:
                return [[]] * (not n)

            return [concat + [num] for num in range(1, capcity) for concat in concatenate(k - 1, n - num, num)]

        return concatenate(k, n, 10)

    def combination_sum_3(self, k, n):

        def helper(combination, k, n, start):
            if k == 0 and n == 0:
                result.append(list(combination))
            else:
                i = start
                while i < len(nums) and n > 0 and k > 0:
                    combination.append(nums[i])
                    helper(combination, k - 1, n - nums[i], i + 1)
                    combination.pop()
                    i += 1

        nums = [num for num in range(1, 10)]
        result = []
        helper([], k, n, 0)
        return result


print(Solution().combination_sum_3(3, 9))
