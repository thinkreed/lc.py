# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = [root]

        while len(q) != 0:
            r = q.pop(0)

            if r.right:
                q.append(r.right)

            if r.left:
                q.append(r.left)

        return r.val
