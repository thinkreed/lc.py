# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False

        q = [root]
        s = set()

        for node in q:
            if k - node.val in s:
                return True

            s.add(node.val)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return False
