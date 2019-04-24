class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return "".join(chr(ord(x) + 32) if 65 <= ord(x) <= 90 else x for x in str)
