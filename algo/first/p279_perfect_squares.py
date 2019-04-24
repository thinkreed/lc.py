from math import sqrt


class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        def is_square(x):
            root = int(sqrt(x))
            return root * root == x

        if is_square(n):
            return 1

        while (n & 3) == 0:
            n >>= 2

        if (n & 7) == 7:
            return 4

        root = int(sqrt(n))

        for i in range(1, root + 1):
            if is_square(n - i * i):
                return 2

        return 3
