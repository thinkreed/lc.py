class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0

        pass_dict = {}

        start_index = 0

        for i, c in enumerate(s):
            if c in pass_dict and start_index <= pass_dict[c]:
                start_index = pass_dict[c] + 1
            else:
                max_len = max(max_len, i - start_index + 1)

            pass_dict[c] = i

        return max_len
