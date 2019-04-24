class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9

        if n == 2:
            return 987

        for i in range(2, 9 * 10 ** (n - 1)):
            higher = 10 ** n - i
            lower = int(str(higher)[::-1])
            if (i ** 2 - 4 * lower) < 0:
                continue

            if (i ** 2 - 4 * lower) ** .5 == int((i ** 2 - 4 * lower) ** .5):
                return (lower + 10 ** n * (10 ** n - i)) % 1337


print(Solution().largestPalindrome(8))