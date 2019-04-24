class Solution:
    def checkValidString(self, str):
        """
        :type str: str
        :rtype: int
        """
        low = 0
        high = 0
        for i in range(len(str)):
            if str[i] == "(":
                low += 1
                high += 1
            elif str[i] == ")":
                if low > 0:
                    low -= 1
                high -= 1
            else:
                if low > 0:
                    low -= 1
                high += 1
            if high < 0:
                return False

        return low == 0
