# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self.deep_first_search_height(root) != -1

    def deep_first_search_height(self, root):
        if not root:
            return 0

        left_subtree_height = self.deep_first_search_height(root.left)
        if left_subtree_height == -1:
            return -1

        right_subtree_height = self.deep_first_search_height(root.right)
        if right_subtree_height == -1:
            return -1

        if abs(right_subtree_height - left_subtree_height) > 1:
            return -1

        return max(left_subtree_height, right_subtree_height) + 1
