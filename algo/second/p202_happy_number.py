class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def countSquareSum(num):
            res = 0
            tmp = 0

            while num:
                tmp = num % 10
                res += tmp * tmp
                num /= 10

            return res

        slow = fast = n

        slow = countSquareSum(slow)
        fast = countSquareSum(fast)
        fast = countSquareSum(fast)

        while slow != fast:
            slow = countSquareSum(slow)
            fast = countSquareSum(fast)
            fast = countSquareSum(fast)

        return slow == 1
