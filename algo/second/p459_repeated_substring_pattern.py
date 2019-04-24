class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tmp = (s + s)[1:-1]

        return tmp.find(s) != -1
