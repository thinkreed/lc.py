class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.first = None
        self.second = None
        self.prev = TreeNode(float('-inf'))

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        def helper(node):
            if not node:
                return

            helper(node.left)

            if self.first is None and self.prev.val >= node.val:
                self.first = self.prev

            if self.first is not None and self.prev.val >= node.val:
                self.second = node

            self.prev = node

            helper(node.right)

        helper(root)

        self.first.val, self.second.val = self.second.val, self.first.val
