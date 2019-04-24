# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def pre_order(root):
            if not root:
                return None

            res.append(root.val)
            pre_order(root.left)
            pre_order(root.right)

        pre_order(root)

        return ' '.join(map(str, res))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        res = deque(int(v) for v in data.split())

        def build(low_bound, high_bound):
            if res and low_bound < res[0] < high_bound:
                v = res.popleft()
                node = TreeNode(v)
                node.left = build(low_bound, v)
                node.right = build(v, high_bound)
                return node

        return build(float('-infinity'), float('infinity'))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
