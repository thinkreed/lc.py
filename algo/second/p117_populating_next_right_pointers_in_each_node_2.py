"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        node = root
        while node:
            cur = tmp = Node(0)
            while node:
                if node.left:
                    cur.next = node.left
                    cur = node.left
                if node.right:
                    cur.next = node.right
                    cur = node.right
                node = node.next
            node = tmp.next

        return root
