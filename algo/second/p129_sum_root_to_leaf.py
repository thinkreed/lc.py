# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = 0

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def helper(node, val):
            if not node:
                return

            helper(node.left, val * 10 + node.val)
            helper(node.right, val * 10 + node.val)
            if not node.left and not node.right:
                self.res += val * 10 + node.val

        helper(root, 0)
        return self.res
