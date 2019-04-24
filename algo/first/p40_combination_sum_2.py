class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def helper(index, path, target):
            if target == 0:
                res.append(path)
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                helper(i + 1, path + [candidates[i]], target - candidates[i])

        candidates = sorted(candidates)
        res = []
        helper(0, [], target)
        return res
