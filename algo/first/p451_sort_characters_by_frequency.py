from collections import Counter


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        char_frequency = Counter(s)
        repeated_segments = {}

        for c, count in char_frequency.items():
            repeated_segments.setdefault(count, []).append(c * count)

        return ''.join([''.join(repeated_segments[i]) for i in range(len(s), -1, -1) if i in repeated_segments])
