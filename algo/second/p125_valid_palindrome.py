import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = " ".join(re.findall("[a-zA-Z0-9]+", s)).lower()
        s = s.replace(" ", "")

        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
