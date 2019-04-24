# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        s = []

        p = root

        while len(s) > 0 or p is not None:
            if p:
                s.append(p)
                res.insert(0, p.val)
                p = p.right
            else:
                node = s.pop()
                p = node.left

        return res
