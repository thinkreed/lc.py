# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self):
        self.tmp = -float('inf')
        self.res = float('inf')

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root.left:
            self.minDiffInBST(root.left)

        self.res = min(self.res, root.val - self.tmp)
        self.tmp = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.res
