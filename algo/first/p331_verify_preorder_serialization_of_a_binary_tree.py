class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(',')
        slots = 1

        for node in nodes:
            if slots == 0:
                return False

            if node == '#':
                slots -= 1
            else:
                slots += 1

        return slots == 0
