class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        candidates = sorted(candidates)

        def dfs(tar, stack):
            if tar == 0:
                res.append(stack)
                return

            for c in candidates:
                if c > tar:
                    break

                if stack and c < stack[-1]:
                    continue

                else:
                    dfs(tar - c, stack + [c])

        dfs(target, [])
        return res
