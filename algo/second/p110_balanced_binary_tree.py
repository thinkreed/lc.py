# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(node):
            if not node:
                return 0

            l = helper(node.left)
            r = helper(node.right)

            if l == -1 or r == -1 or abs(l - r) > 1:
                return -1

            return 1 + max(l, r)

        return helper(root) != -1
