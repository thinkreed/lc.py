class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)

        step = 0
        sumary = 0

        while sumary < target:
            step += 1
            sumary += step

        while (sumary - target) % 2 != 0:
            step += 1
            sumary += step

        return step
