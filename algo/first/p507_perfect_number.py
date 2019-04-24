class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return False
        sumary = 1

        i = 2
        while i * i <= num:
            if num % i == 0:
                sumary += i
                sumary += num // i
            i += 1

        return sumary == num
