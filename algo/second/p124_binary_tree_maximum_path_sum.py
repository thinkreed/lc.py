# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.max_val = float('-inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def max_path_down(node):
            if not node:
                return 0

            left = max(0, max_path_down(node.left))
            right = max(0, max_path_down(node.right))

            self.max_val = max(self.max_val, left + right + node.val)
            return max(left, right) + node.val

        max_path_down(root)
        return self.max_val
