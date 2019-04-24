class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0

    def is_perfect_square(self, num):
        low, high = 1, num

        while low <= high:
            mid = (low + high) >> 1
            current = mid * mid

            if current == num:
                return True
            elif current < num:
                low = mid + 1
            else:
                high = mid - 1
        return False
