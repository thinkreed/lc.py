# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def rob_child(root):
            if not root:
                return 0, 0

            rob_left_child = rob_child(root.left)
            rob_right_child = rob_child(root.right)

            root_robbed = root.val + rob_left_child[1] + rob_right_child[1]
            root_not_robbed = max(rob_left_child[0], rob_left_child[1]) + max(rob_right_child[1], rob_right_child[0])

            return root_robbed, root_not_robbed

        value = rob_child(root)
        return max(value[0], value[1])
