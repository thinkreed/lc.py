# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        cur = root
        pre = None
        prev = None

        while cur:
            if cur.left is None:
                if prev and prev.val >= cur.val:
                    return False
                prev = cur
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right

                if pre.right == cur:
                    if prev and prev.val >= cur.val:
                        return False

                    prev = cur
                    cur = cur.right
                else:
                    pre.right = cur
                    cur = cur.left

        return True
