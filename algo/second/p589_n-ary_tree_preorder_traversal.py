"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        s = root and [root]

        while s:
            n = s.pop()
            res.append(n.val)
            s += [c for c in n.children[::-1] if c]

        return res
