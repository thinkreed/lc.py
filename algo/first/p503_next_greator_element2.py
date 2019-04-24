class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = len(nums)
        result = [-1] * count

        stack = []

        for i in range(2 * count):
            num = nums[i % count]
            while len(stack) > 0 and nums[stack[-1]] < num:
                result[stack.pop()] = num

            if i < count:
                stack.append(i)

            if len(stack) == 0:
                break

        return result
