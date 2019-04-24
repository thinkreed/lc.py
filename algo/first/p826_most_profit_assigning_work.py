class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        jobs = sorted([diff, pro] for diff, pro in zip(difficulty, profit))
        res = 0
        i = 0
        max_profit = 0

        for ability in sorted(worker):
            while i < len(jobs) and ability >= jobs[i][0]:
                max_profit = max(jobs[i][1], max_profit)
                i += 1
            res += max_profit

        return res
