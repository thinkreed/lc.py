class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        dp = []
        candidates = sorted(candidates)

        t_max = max(target + 1, max(candidates) + 1)

        for _ in range(t_max):
            dp.append([])

        for num in candidates:
            dp[num].append((num,))

            for i in range(1, target - num + 1):
                for prev in dp[i]:
                    dp[i + num].append(prev + (num,))

        return dp[target]
