# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        q = [root]

        while any(q):
            result.append(max(node.val for node in q))
            q = [child for node in q for child in (node.left, node.right) if child]

        return result
