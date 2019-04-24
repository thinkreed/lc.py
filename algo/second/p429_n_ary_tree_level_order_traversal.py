"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        queue = [root]
        res = []

        while any(queue):
            res.append([node.val for node in queue])
            queue = [child for node in queue for child in node.children if child]

        return res
