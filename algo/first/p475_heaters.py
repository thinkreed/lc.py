class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        sorted_houses = sorted(houses)
        sorted_heaters = sorted(heaters)

        i = 0
        result = 0
        for house in sorted_houses:
            while (i < len(sorted_heaters) - 1) and (sorted_heaters[i] + sorted_heaters[i + 1] <= house * 2):
                i += 1
            result = max(result, abs(sorted_heaters[i] - house))

        return result
