# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.visit = root
        self.stack = []

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        while self.visit:
            self.stack.append(self.visit)
            self.visit = self.visit.left

        next = self.stack.pop()
        self.visit = next.right
        return next.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.visit or len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
