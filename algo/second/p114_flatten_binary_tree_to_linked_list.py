# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        node = root

        while node:
            if node.left:
                l, r = node.left, node.right
                node.left, node.right = None, l
                while l.right:
                    l = l.right

                l.right = r

            node = node.right
