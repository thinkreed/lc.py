# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self):
        self.tmp = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        if root.right:
            self.convertBST(root.right)

        root.val += self.tmp
        self.tmp = root.val

        if root.left:
            self.convertBST(root.left)

        return root
