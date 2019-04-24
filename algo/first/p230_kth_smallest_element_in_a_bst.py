# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def helper(node, vals):
            if not node:
                return

            helper(node.left, vals)
            vals.append(node.val)
            helper(node.right, vals)

        values = []
        helper(root, values)
        return values[k - 1]
