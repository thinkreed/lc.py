class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(set(s)) != len(set(t)):
            return False

        dic = {}

        for i, c in enumerate(s):
            if c not in dic:
                dic[c] = t[i]
            elif dic[c] != t[i]:
                return False

        return True
