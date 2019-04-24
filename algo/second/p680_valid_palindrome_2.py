class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        r = s[::-1]

        if s == r:
            return True

        half_len = len(s) // 2

        for i in range(half_len):
            if s[i] != r[i]:
                if s[i + 1:half_len + 1] == r[i:half_len]:
                    return True

                if s[i:half_len] == r[i + 1:half_len + 1]:
                    return True

                return False
