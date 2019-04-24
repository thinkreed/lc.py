class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        i = 0
        number_of_spots = len(flowerbed)

        while i < number_of_spots and count < n:
            if flowerbed[i] == 0:
                is_next_placed = False if i == number_of_spots - 1 else flowerbed[i + 1] == 1
                is_prev_placed = False if i == 0 else flowerbed[i - 1] == 1
                if not is_prev_placed and not is_next_placed:
                    flowerbed[i] = 1
                    count += 1
            i += 1

        return count == n
