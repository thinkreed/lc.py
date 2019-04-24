class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        common_m, common_n = m, n
        for operation in ops:
            if operation[0] < common_m:
                common_m = operation[0]
            if operation[1] < common_n:
                common_n = operation[1]

        return common_m * common_n
