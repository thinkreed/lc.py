class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        c = ord(t[-1])

        for i in range(len(s)):
            c ^= ord(s[i])
            c ^= ord(t[i])

        return chr(c)
