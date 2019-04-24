class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels_set = 'aeiouAEIOU'
        i, j = 0, len(s) - 1
        s = list(s)
        while i < j:
            while s[i] not in vowels_set and i < j:
                i += 1
            while s[j] not in vowels_set and i < j:
                j -= 1
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1
        return ''.join(s)
