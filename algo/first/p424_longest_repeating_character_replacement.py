from collections import Counter


class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start = 0
        end = 0

        counts = Counter()

        for end in range(1, len(s) + 1):
            counts[s[end - 1]] += 1
            max_repeat_char = counts.most_common(1)[0][1]

            if end - start - max_repeat_char > k:
                counts[s[start]] -= 1
                start += 1

        return end - start
