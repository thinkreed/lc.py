"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        s = [root]

        while s:
            node = s.pop()
            res.append(node.val)
            s.extend(node.children)

        return res[::-1]
