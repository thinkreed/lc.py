# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def generate(start, end):
            res = []
            for root in range(start, end + 1):
                for left in generate(start, root - 1):
                    for right in generate(root + 1, end):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        res += node,
            return res or [None]

        return generate(1, n)
