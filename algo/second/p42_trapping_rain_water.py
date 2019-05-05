class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1

        level = 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                lower = height[left]
                left += 1
            else:
                lower = height[right]
                right -= 1

            level = max(level, lower)
            water += level - lower

        return water
