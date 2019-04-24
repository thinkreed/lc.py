class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        res = ''

        for item in d:
            if (-len(item), item) < (-len(res), res):
                it = iter(s)
                if all(c in it for c in item):
                    res = item

        return res
