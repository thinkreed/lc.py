class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        counts = [0] * 26
        ord_a = ord('a')
        result = ''

        for char in T:
            counts[ord(char) - ord_a] += 1

        for c in S:
            while counts[ord(c) - ord_a] > 0:
                result += c
                counts[ord(c) - ord_a] -= 1

        for i in range(26):
            while counts[i] > 0:
                result += chr(ord_a + i)
                counts[i] -= 1

        return result
