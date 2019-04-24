class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_of_segments = 0

        for i, c in enumerate(s):
            if c != ' ' and (i == 0 or s[i - 1] == ' '):
                count_of_segments += 1

        return count_of_segments
