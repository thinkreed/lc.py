class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = str.split()

        return len(pattern) == len(s) and len(set(s)) == len(set(pattern)) == len(set(zip(pattern, s)))
