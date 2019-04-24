class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        s_length = len(s)
        p_length = len(p)
        if s_length < p_length:
            return result

        p_hash = [0] * 123
        s_hash = [0] * 123

        for c in p:
            p_hash[ord(c)] += 1

        for c in s[:p_length - 1]:
            s_hash[ord(c)] += 1

        for i in range(p_length - 1, s_length):
            s_hash[ord(s[i])] += 1

            if i - p_length >= 0:
                s_hash[ord(s[i - p_length])] -= 1

            if s_hash == p_hash:
                result.append(i - p_length + 1)
        return result
