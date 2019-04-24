class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        if K == 0 or N >= K + W: return 1
        dic = [1.0] + [0.0] * N
        sumary = 1.0
        for i in range(1, N + 1):
            dic[i] = sumary / W
            if i < K:
                sumary += dic[i]
            if i - W >= 0:
                sumary -= dic[i - W]
        return sum(dic[K:])
