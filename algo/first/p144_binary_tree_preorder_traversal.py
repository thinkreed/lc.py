# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        right_nodes = []
        result = []
        current = root

        while current or right_nodes:
            if not current:
                current = right_nodes.pop()

            while current:
                result.append(current.val)
                if current.right:
                    right_nodes.append(current.right)
                current = current.left

        return result
