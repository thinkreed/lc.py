class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        pass_dict = {}
        longest_length = substring_start = 0
        for i, c in enumerate(s):
            if c in pass_dict and substring_start <= pass_dict[c]:
                substring_start = pass_dict[c] + 1
            else:
                longest_length = max(longest_length, i - substring_start + 1)
            pass_dict[c] = i

        return longest_length
