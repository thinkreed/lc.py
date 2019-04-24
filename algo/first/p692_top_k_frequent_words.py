from collections import Counter


class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counts = Counter(words)
        pairs = list(counts.items())
        pairs.sort(key=lambda pair: (-pair[1], pair[0]))
        return [pair[0] for pair in pairs[0:k]]
