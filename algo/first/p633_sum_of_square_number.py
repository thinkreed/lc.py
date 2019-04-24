class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i = 0
        member_dict = {}

        while i * i <= c:
            member_dict[i * i] = i
            if (c - i * i) in member_dict:
                return True

            i += 1

        return False
