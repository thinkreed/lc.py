class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen = set()
        repeated = set()

        for i in range(0, len(s) - 9):
            ten = s[i:i + 10]
            if ten in seen:
                repeated.add(ten)

            seen.add(ten)

        return list(repeated)
