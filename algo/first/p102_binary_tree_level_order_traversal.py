# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        level = [root]

        while root and level:
            res.append([node.val for node in level])
            level = [child for node in level for child in (node.left, node.right) if child]

        return res
