"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        q = deque([root])

        while q:
            tmp_q = []
            q_len = len(q)

            for i in range(q_len):
                if i != q_len - 1:
                    q[i].next = q[i + 1]
                node = q[i]
                if node:
                    tmp_q.extend([node.left, node.right])
            q = [node for node in tmp_q if node]

        return root
