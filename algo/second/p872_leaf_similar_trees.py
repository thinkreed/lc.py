# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        def helper(root):
            if not root:
                return ''
            if not (root.left or root.right):
                return str(root.val)

            return helper(root.left) + helper(root.right)

        return helper(root1) == helper(root2)
