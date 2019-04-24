class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        result = []

        low = 1
        high = n
        while low <= high:
            if k <= 1:
                result.append(low)
                low += 1
            else:
                if k % 2 == 0:
                    result.append(high)
                    high -= 1
                else:
                    result.append(low)
                    low += 1
                k -= 1

        return result
