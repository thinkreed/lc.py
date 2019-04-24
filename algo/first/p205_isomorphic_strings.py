class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dic = {}
        t_dic = {}

        for i in range(len(s)):
            s_dic[s[i]] = i + 1
            t_dic[t[i]] = i + 1

        for i in range(len(s)):
            if s_dic[s[i]] != t_dic[t[i]]:
                return False

        return True
