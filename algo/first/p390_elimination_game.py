class Solution:
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        from_left = True
        count = n
        step = 1
        head = 1

        while count > 1:
            if from_left or (count & 1) == 1:
                head += step

            count >>= 1
            step <<= 1
            from_left = not from_left

        return head
