# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        stack = []

        prev = None

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            if prev and root.val <= prev.val:
                return False

            prev = root
            root = root.right

        return True
