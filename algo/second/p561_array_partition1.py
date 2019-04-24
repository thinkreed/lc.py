class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        exist = [0] * 20001

        for n in nums:
            exist[n + 10000] += 1

        sumary = 0
        odd = True
        for i in range(len(exist)):
            while exist[i] > 0:
                if odd:
                    sumary += i - 10000

                odd = not odd
                exist[i] -= 1

        return sumary
