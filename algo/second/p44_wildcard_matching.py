class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_len = len(s)
        p_len = len(p)

        i = 0
        j = 0
        match = 0
        start_index = -1

        while i < s_len:
            if j < p_len and (p[j] == '?' or s[i] == p[j]):
                i += 1
                j += 1
            elif j < p_len and p[j] == '*':
                start_index = j
                match = i
                j += 1
            elif start_index != -1:
                j = start_index + 1
                match += 1
                i = match
            else:
                return False

        while j < p_len and p[j] == '*':
            j += 1

        return j == p_len
