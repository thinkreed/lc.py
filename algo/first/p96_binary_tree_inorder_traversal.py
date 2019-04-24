# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        current = root
        while current:
            if not current.left:
                result.append(current.val)
                current = current.right
            else:
                previous = current.left
                while previous.right and previous.right != current:
                    previous = previous.right

                if not previous.right:
                    previous.right = current
                    current = current.left
                else:
                    previous.right = None
                    result.append(current.val)
                    current = current.right

        return result
