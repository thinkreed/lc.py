class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        count_of_one = 0
        i = len(bits) - 2
        while i >= 0 and bits[i] != 0:
            count_of_one += 1
            i -= 1

        if count_of_one % 2 > 0:
            return False

        return True
