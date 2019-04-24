# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        def helper(root, level, cache):
            if root:
                if len(cache) < level + 1:
                    cache.insert(0, [])

                cache[-(level + 1)].append(root.val)
                helper(root.left, level + 1, cache)
                helper(root.right, level + 1, cache)

        res = []
        helper(root, 0, res)
        return res
