class Solution:
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        count = [0] * 26
        max_len_current = 0

        for i in range(len(p)):
            if i > 0 and (ord(p[i]) - ord(p[i - 1]) == 1) or (ord(p[i - 1]) - ord(p[i]) == 25):
                max_len_current += 1
            else:
                max_len_current = 1

            index = ord(p[i]) - ord('a')
            count[index] = max(count[index], max_len_current)

        return sum(count)
