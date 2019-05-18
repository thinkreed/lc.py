from collections import defaultdict


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ''

        count_dic = defaultdict(int)

        for c in t:
            count_dic[c] += 1

        missing = len(t)

        start = 0
        end = float('inf')
        cur_start = 0

        for cur_end, c in enumerate(s, 1):
            if count_dic[c] > 0:
                missing -= 1

            count_dic[c] -= 1

            if missing == 0:
                while count_dic[s[cur_start]] < 0:
                    count_dic[s[cur_start]] += 1
                    cur_start += 1

                if cur_end - cur_start < end - start:
                    start, end = cur_start, cur_end

                count_dic[s[cur_start]] += 1
                missing += 1
                cur_start += 1

        return s[start:end] if end != float('inf') else ''
