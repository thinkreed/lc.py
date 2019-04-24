class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        flowerbed.insert(0, 0)
        flowerbed.append(0)

        count = 0

        for p in flowerbed:
            if p == 0:
                count += 1
            else:
                count = 0

            if count == 3:
                n -= 1
                count = 1

            if n == 0:
                return True

        return False
