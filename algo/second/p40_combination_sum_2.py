class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        candidates = sorted(candidates)

        s_len = len(candidates)

        def dfs(tar, index, tmp):

            if tar == 0:
                res.append(tmp)
                return

            for i in range(index, s_len):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > tar:
                    break
                dfs(tar - candidates[i], i + 1, tmp + [candidates[i]])

        dfs(target, 0, [])
        return res
