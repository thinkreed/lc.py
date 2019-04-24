class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        level = [(1, root)]
        while level:
            res = max(res, level[-1][0] - level[0][0] + 1)
            level = [child for num, node in level for child in enumerate((node.left, node.right), 2 * num) if child[1]]

        return res
