# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        def helper(node, path, res):
            if not node.left and not node.right:
                res.append(path + str(node.val))

            if node.left:
                helper(node.left, path + str(node.val) + '->', res)

            if node.right:
                helper(node.right, path + str(node.val) + '->', res)

        if not root:
            return []

        res = []
        helper(root, '', res)
        return res
