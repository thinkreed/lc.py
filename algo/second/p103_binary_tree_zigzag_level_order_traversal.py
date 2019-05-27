# Definition for a binary tree node.

from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        q = deque()

        q.append(root)

        res = []
        i = 0

        while q:
            n = len(q)
            level = []

            i = (i + 1) % 2

            for _ in range(n):
                cur = q.popleft()
                level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            if i == 0:
                level.reverse()

            res.append(level)

        return res
