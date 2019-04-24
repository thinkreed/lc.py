class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''

        first = strs[0]
        f_len = len(first)

        for s in strs:
            not_same = True

            while not_same:
                if first[0:f_len] == s[0:f_len]:
                    not_same = False
                else:
                    f_len -= 1

        return first[0:f_len]
