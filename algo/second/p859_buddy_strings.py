class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False

        if A == B and len(set(A)) < len(A):
            return True

        diffs = [(i, j) for i, j in zip(A, B) if i != j]

        return len(diffs) == 2 and diffs[0] == diffs[1][::-1]
