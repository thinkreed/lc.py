from collections import Counter


class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        def min_window(s, t):
            need = Counter(t)
            miss_sum = len(t)
            i = 0
            left = 0
            right = 0
            for j, c in enumerate(s, 1):
                miss_sum -= need[c] > 0
                need[c] -= 1
                if not miss_sum:
                    while i < j and need[s[i]] < 0:
                        need[s[i]] += 1
                        i += 1
                    if not right or j - i <= right - left:
                        left, right = i, j
            return s[left:right]

        return len(min_window(s2, s1)) == len(s1)
