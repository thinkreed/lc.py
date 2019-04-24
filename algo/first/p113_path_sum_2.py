# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        def helper(node, target):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right and node.val == target:
                res.append(list(path))
                path.pop()
                return
            else:
                helper(node.left, target - node.val)
                helper(node.right, target - node.val)
            path.pop()

        res = []
        path = []

        helper(root, sum)
        return res
