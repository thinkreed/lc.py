class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        i = len(S) - 1
        j = len(T) - 1

        count_s = 0
        count_t = 0

        while True:
            while i >= 0 and (count_s or S[i] == '#'):
                count_s += 1 if S[i] == '#' else -1
                i -= 1

            while j >= 0 and (count_t or T[j] == '#'):
                count_t += 1 if T[j] == '#' else -1
                j -= 1

            if not (i >= 0 and j >= 0 and S[i] == T[j]):
                return i == j == -1

            i -= 1
            j -= 1
