# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        q = [root]
        res = []
        while q:
            cur = q.pop()
            res.append(cur.val)
            if cur.right:
                q.append(cur.right)

            if cur.left:
                q.append(cur.left)

        return res
