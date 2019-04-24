# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []

        q = [root]

        while any(q):
            res.append(sum([node.val for node in q]) / (len(q) * 1.0))
            q = [child for node in q for child in (node.left, node.right) if child]

        return res
