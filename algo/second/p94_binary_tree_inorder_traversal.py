# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def helper(node, res):
            if not node:
                return

            helper(node.left, res)
            res.append(node.val)
            helper(node.right, res)

        res = []

        helper(root, res)
        return res
