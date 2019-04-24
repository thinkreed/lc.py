class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        temp_pattern = pattern
        temp_str = str.split()
        return map(temp_pattern.find, temp_pattern) == map(temp_str.index, temp_str)
