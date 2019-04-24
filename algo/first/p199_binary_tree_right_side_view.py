# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def helper(node, depth):
            if not node:
                return

            if depth == len(right_view):
                right_view.append(node.val)
            helper(node.right, depth + 1)
            helper(node.left, depth + 1)

        right_view = []
        helper(root, 0)
        return right_view
