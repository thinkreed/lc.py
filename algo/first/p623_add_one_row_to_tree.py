class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        temp = TreeNode(None)
        temp.left = root

        row = [temp]

        for _ in range(d - 1):
            row = [child for node in row for child in (node.left, node.right) if child]

        for node in row:
            node.left, node.left.left = TreeNode(v), node.left
            node.right, node.right.right = TreeNode(v), node.right

        return temp.left
