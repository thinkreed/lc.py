from collections import Counter


class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        counts = Counter((A + " " + B).split())
        return [word for word in counts if counts[word] == 1]
