class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = len(nums)
        result = []

        product_of_left = 1

        for i, num in enumerate(nums):
            if i > 0:
                product_of_left *= nums[i - 1]

            result.append(product_of_left)

        product_of_right = 1

        for i in range(count - 1, -1, -1):
            if i < count - 1:
                product_of_right *= nums[i + 1]
            result[i] *= product_of_right

        return result
