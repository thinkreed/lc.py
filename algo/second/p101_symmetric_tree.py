# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(left, right):
            if not left or not right:
                return left == right

            if left.val != right.val:
                return False

            return helper(left.left, right.right) and helper(left.right, right.left)

        return not root or helper(root.left, root.right)
