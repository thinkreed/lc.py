class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = ['']

        for c in S:
            if c.isalpha():
                res = [i + j for i in res for j in (c.lower(), c.upper())]
            else:
                res = [i + c for i in res]

        return res
