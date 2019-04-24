# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node, current):
            if node.left is None and node.right is None:
                return 10 * current + node.val

            val = 0
            if node.left:
                val += dfs(node.left, 10 * current + node.val)
            if node.right:
                val += dfs(node.right, 10 * current + node.val)

            return val

        if not root:
            return 0

        return dfs(root, 0)
