class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """

    def fibonacci(self, n):
        # write your code here
        if n == 1:
            return 0
        if n == 2:
            return 1
        one = 0
        two = 1
        res = 0
        for i in range(3, n + 1):
            res = one + two
            one = two
            two = res

        return res
