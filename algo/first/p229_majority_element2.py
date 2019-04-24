class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        c1 = 0
        c2 = 0
        pick1 = 0
        pick2 = 1

        for num in nums:
            if num == pick1:
                c1 += 1
            elif num == pick2:
                c2 += 1
            elif c1 == 0:
                pick1 = num
                c1 = 1
            elif c2 == 0:
                pick2 = num
                c2 = 1
            else:
                c1 = c1 - 1
                c2 = c2 - 1

        return [x for x in (pick1, pick2) if nums.count(x) > len(nums) // 3]
