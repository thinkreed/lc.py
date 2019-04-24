class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        if len(S) == 0:
            return []

        p = 0
        count = 1
        tmp = S[0]
        res = []

        for i, c in enumerate(S[1:]):
            if c == tmp:
                count += 1
            elif count >= 3:
                res.append([p, i])
                count = 1
                p = i + 1
                tmp = c
            else:
                count = 1
                p = i + 1
                tmp = c

        if count >= 3:
            res.append([p, len(S) - 1])

        return res
