class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = None
        count = 0

        for num in nums:
            if num == res:
                count += 1
            elif count == 0:
                res = num
                count = 1
            else:
                count -= 1

        return res
