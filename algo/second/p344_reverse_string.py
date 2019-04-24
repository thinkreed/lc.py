class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        res = list(s)

        i = 0
        j = len(s) - 1

        while i < j:
            res[i], res[j] = res[j], res[i]
            i += 1
            j -= 1

        return "".join(res)
