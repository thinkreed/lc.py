class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        res = []

        for digit in num:
            while k and res and res[-1] > digit:
                res.pop()
                k -= 1

            res.append(digit)

        return ''.join(res[:-k or None]).lstrip('0') or '0'
