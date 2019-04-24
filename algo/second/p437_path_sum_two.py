class Solution(object):

    def __init__(self):
        self.res = 0

    def pathSum(self, root, sum):
        cache = {0: 1}

        self.dfs(root, sum, 0, cache)

        return self.res

    def dfs(self, root, target, cur_sum, cache):
        if not root:
            return
        cur_sum += root.val
        old_sum = cur_sum - target
        self.res += cache.get(old_sum, 0)
        cache[cur_sum] = cache.get(cur_sum, 0) + 1

        self.dfs(root.left, target, cur_sum, cache)
        self.dfs(root.right, target, cur_sum, cache)
        cache[cur_sum] -= 1
