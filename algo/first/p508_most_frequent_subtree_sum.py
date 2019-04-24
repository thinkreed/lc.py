# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import Counter


class Solution(object):

    def __init__(self):
        self.counter = Counter()

    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        self.helper(root)
        most_frequent_count = max(self.counter.values())
        return [sum_of_root for sum_of_root in self.counter.keys() if self.counter[sum_of_root] == most_frequent_count]

    def helper(self, root):
        if not root:
            return 0

        sum_of_root = root.val + self.helper(root.left) + self.helper(root.right)
        self.counter[sum_of_root] += 1
        return sum_of_root
