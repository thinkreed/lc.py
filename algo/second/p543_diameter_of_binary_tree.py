# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self):
        self.res = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def helper(root):
            if not root:
                return 0

            left = helper(root.left)
            right = helper(root.right)

            self.res = max(self.res, left + right)

            return max(left, right) + 1

        helper(root)
        return self.res
