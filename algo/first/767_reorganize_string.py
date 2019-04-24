from collections import Counter


class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        counts = Counter(S)
        if max(counts.values()) <= (len(S) + 1) // 2:
            res = ""
            while counts:
                pairs = counts.most_common(2)
                if len(pairs):
                    res += pairs[0][0]
                    counts[pairs[0][0]] -= 1

                if len(pairs) > 1:
                    res += pairs[1][0]
                    counts[pairs[1][0]] -= 1

                counts += Counter()
            return res
        return ""
