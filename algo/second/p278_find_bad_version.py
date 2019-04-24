# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        j = n

        while i < j:
            mid = (i + j) // 2

            if isBadVersion(mid) == False:
                i = mid + 1
            else:
                j = mid

        if isBadVersion(i):
            return i

        return i + 1
