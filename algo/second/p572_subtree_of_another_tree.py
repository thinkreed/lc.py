# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        def helper(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val != q.val:
                return False

            return helper(p.left, q.left) and helper(p.right, q.right)

        if not s:
            return False

        if helper(s, t):
            return True

        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
