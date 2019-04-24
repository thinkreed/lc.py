# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res = []

        q = [root]
        left_to_right = True

        while len(q) > 0:
            size = len(q)
            row = [0] * size
            for i in range(size):
                node = q.pop(0)
                index = i if left_to_right else size - 1 - i

                row[index] = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            left_to_right = not left_to_right
            res.append(row)

        return res
