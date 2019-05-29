# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res

        def dfs(node, path, cur_sum):
            cur_sum += node.val

            if node.left or node.right:
                if node.left:
                    dfs(node.left, path + [node.val], cur_sum)

                if node.right:
                    dfs(node.right, path + [node.val], cur_sum)
            else:
                if cur_sum == sum:
                    res.append(path + [node.val])

        dfs(root, [], 0)
        return res
