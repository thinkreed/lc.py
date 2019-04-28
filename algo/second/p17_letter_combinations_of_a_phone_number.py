class Solution(object):

    def __init__(self):
        self.dic = {'2': list('abc'), '3': list('def'),
                    '4': list('ghi'), '5': list('jkl'), '6': list('mno'),
                    '7': list('pqrs'), '8': 'tuv', '9': list('wxyz')}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        res = []
        d_len = len(digits)

        def helper(i, cur):
            if i == d_len:
                res.append(cur)
                return

            for c in self.dic[digits[i]]:
                helper(i + 1, cur + c)

        helper(0, '')

        return res
