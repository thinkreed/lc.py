class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        count = 0

        for c in word:
            if c == c.upper():
                count += 1

        return count == len(word) or count == 0 or (count == 1 and word[0] == word[0].upper())
