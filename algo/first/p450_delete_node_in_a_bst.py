# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                return root.left

            if not root.left:
                return root.right

            node = root.right
            min_right = node.val

            while node.left:
                node = node.left
                min_right = node.val

            root.val = min_right
            root.right = self.deleteNode(root.right, root.val)
        return root
