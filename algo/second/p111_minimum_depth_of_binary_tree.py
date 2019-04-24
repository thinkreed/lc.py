# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        q = [root]

        res = 1

        while q:
            for i in range(len(q)):
                node = q.pop(0)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

                if not node.left and not node.right:
                    return res

            res += 1

        return res
