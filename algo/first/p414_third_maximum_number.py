class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = None
        two = None
        three = None

        for num in nums:
            if num == one or num == two or num == three:
                continue

            if not one or num > one:
                three = two
                two = one
                one = num
            elif not two or num > two:
                three = two
                two = num
            elif not three or num > three:
                three = num

        return three if three is not None else one
