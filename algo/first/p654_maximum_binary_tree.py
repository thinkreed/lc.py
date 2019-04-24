# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        help_stack = []
        for num in nums:
            current_node = TreeNode(num)
            while len(help_stack) > 0 and help_stack[-1].val < num:
                current_node.left = help_stack.pop()

            if len(help_stack) > 0:
                help_stack[-1].right = current_node

            help_stack.append(current_node)

        return None if len(help_stack) == 0 else help_stack[0]
