class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        return self.deep_first_search(root, root, k)

    def deep_first_search(self, root, current, k):
        if not current:
            return False

        return self.binary_search(root, current, k - current.val) or self.deep_first_search(root, current.left,
                                                                                         k) or self.deep_first_search(
            root, current.right, k)

    def binary_search(self, root, current, value):
        if not root:
            return False

        return (root.val == value and root != current) or \
               (root.val < value and self.binary_search(root.right, current, value)) or \
               (root.val > value and self.binary_search(root.left, current, value))
