# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self):
        self.res = 0

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def helper(node, val):

            if not node:
                return 0

            left = helper(node.left, node.val)
            right = helper(node.right, node.val)

            self.res = max(self.res, left + right)

            if node.val == val:
                return max(left, right) + 1

            return 0

        if not root:
            return 0

        helper(root, root.val)

        return self.res
