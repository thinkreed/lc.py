# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        return self.helper(root, 0, sum, {0: 1})

    def helper(self, root, current_sum, sum, cache):
        if not root:
            return 0

        current_sum += root.val
        result = cache[current_sum - sum] if (current_sum - sum) in cache else 0
        cache[current_sum] = cache[current_sum] + 1 if current_sum in cache else 1
        result += self.helper(root.left, current_sum, sum, cache) + self.helper(root.right, current_sum, sum, cache)
        cache[current_sum] = cache[current_sum] - 1
        return result
