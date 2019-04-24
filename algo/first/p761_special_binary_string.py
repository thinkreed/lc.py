class Solution(object):
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        c = 0
        i = 0
        res = []

        for index, value in enumerate(S):
            c = c + 1 if value == '1' else c - 1
            if c == 0:
                res.append('1' + self.makeLargestSpecial(S[i + 1:index]) + '0')
                i = index + 1

        return ''.join(sorted(res)[::-1])
