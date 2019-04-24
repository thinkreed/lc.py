# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if root is None:
            return 0

        if L <= root.val <= R:
            return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)

        elif root.val < L:
            return self.rangeSumBST(root.right, L, R)

        else:
            return self.rangeSumBST(root.left, L, R)
