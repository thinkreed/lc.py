# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self):
        self.cur_val = 0
        self.cur_count = 0
        self.max_count = 0
        self.mode_count = 0
        self.modes = None

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def handle_values(val):
            if val != self.cur_val:
                self.cur_val = val
                self.cur_count = 0

            self.cur_count += 1

            if self.cur_count > self.max_count:
                self.max_count = self.cur_count
                self.mode_count = 1
            elif self.cur_count == self.max_count:
                if self.modes:
                    self.modes[self.mode_count] = self.cur_val

                self.mode_count += 1

        def in_order(node):
            if not node:
                return

            in_order(node.left)
            handle_values(node.val)
            in_order(node.right)

        in_order(root)
        self.modes = [0] * self.mode_count
        self.mode_count = 0
        self.cur_count = 0
        in_order(root)
        return self.modes
