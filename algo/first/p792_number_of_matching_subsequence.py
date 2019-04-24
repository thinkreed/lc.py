from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        sub_dict = defaultdict(list)
        for it in map(iter, words):
            sub_dict[next(it)].append(it)

        for c in S:
            for it in sub_dict.pop(c, ()):
                sub_dict[next(it, None)].append(it)

        return len(sub_dict[None])
