# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sumary = 0

        def reverse(root):
            if root:
                reverse(root.right)
                root.val += self.sumary
                self.sumary = root.val
                reverse(root.left)

        reverse(root)

        return root
