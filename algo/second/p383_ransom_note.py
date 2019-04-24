class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = [0] * 26
        ord_a = ord('a')

        for c in magazine:
            d[ord(c) - ord_a] += 1

        for c in ransomNote:
            d[ord(c) - ord_a] -= 1

        for c in ransomNote:
            if d[ord(c) - ord_a] < 0:
                return False

        return True
