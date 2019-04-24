class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        for factor in [2, 3, 5]:
            while num % factor == 0:
                num = num / factor

        return num == 1
