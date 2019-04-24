class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = [0] * 26
        ord_a = ord('a')

        for c in s:
            d[ord(c) - ord_a] += 1

        for c in t:
            d[ord(c) - ord_a] -= 1

        for i in range(26):
            if d[i] != 0:
                return False

        return True
