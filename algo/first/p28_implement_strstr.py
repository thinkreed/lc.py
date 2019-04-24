class Solution(object):
    def __init__(self):
        self.lps = None

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length_haystack = len(haystack)
        length_needle = len(needle)
        if length_needle == 0:
            return 0
        self.lps = [0] * length_needle
        self.generate_longest_prefix_suffix_array(needle)
        i = 0
        j = 0
        while i < length_haystack:
            if needle[j] == haystack[i]:
                i += 1
                j += 1
            if j == length_needle:
                return i - j
            elif i < length_haystack and needle[j] != haystack[i]:
                if j != 0:
                    j = self.lps[j - 1]
                else:
                    i += 1
        return -1

    def generate_longest_prefix_suffix_array(self, pattern):
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                self.lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = self.lps[length - 1]
                else:
                    self.lps[i] = 0
                    i += 1
