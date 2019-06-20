class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res = {len(s): ['']}

        def helper(i):
            if i not in res:
                res[i] = [s[i:j] + (tail and ' ' + tail)
                          for j in range(i + 1, len(s) + 1)
                          if s[i:j] in wordDict
                          for tail in helper(j)]
            return res[i]

        return helper(0)
