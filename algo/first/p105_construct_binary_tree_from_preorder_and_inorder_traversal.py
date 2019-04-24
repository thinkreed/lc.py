# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        def helper(prestart, instart, inend):
            if prestart > len(preorder) - 1 or instart > inend:
                return None

            root = TreeNode(preorder[prestart])
            inindex = 0
            for i in range(instart, inend + 1):
                if inorder[i] == root.val:
                    inindex = i

            root.left = helper(prestart + 1, instart, inindex - 1)
            root.right = helper(prestart + inindex - instart + 1, inindex + 1, inend)
            return root

        return helper(0, 0, len(inorder) - 1)


Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
