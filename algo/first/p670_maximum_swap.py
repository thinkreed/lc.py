class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = [int(x) for x in str(num)]
        pairs = {val: i for i, val in enumerate(digits)}
        for i, val in enumerate(digits):
            for d in range(9, val, -1):
                if pairs.get(d, -1) > i:
                    digits[i], digits[pairs[d]] = digits[pairs[d]], digits[i]
                    return int("".join(map(str, digits)))
        return num
