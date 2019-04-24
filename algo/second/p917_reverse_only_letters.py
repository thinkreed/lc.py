class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        s = list(S)

        i = 0
        j = len(S) - 1

        while i < j:
            if not s[i].isalpha():
                i += 1
                continue

            if not s[j].isalpha():
                j -= 1
                continue

            if i >= j:
                break

            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return "".join(s)
