from collections import Counter


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []

        p_len = len(p)
        s_len = len(s)

        s_counter = Counter(s[:p_len - 1])
        p_counter = Counter(p)

        for i in range(p_len - 1, s_len):
            s_counter[s[i]] += 1

            if p_counter == s_counter:
                res.append(i - p_len + 1)

            s_counter[s[i - p_len + 1]] -= 1

            if s_counter[s[i - p_len + 1]] == 0:
                del s_counter[s[i - p_len + 1]]

        return res
