class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num1 = float('inf')
        num2 = float('inf')

        for num in nums:
            if num <= num1:
                num1 = num
            elif num <= num2:
                num2 = num
            else:
                return True

        return False
