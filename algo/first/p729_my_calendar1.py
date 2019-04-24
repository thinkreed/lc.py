class TreeNode(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


def helper(node, start, end):
    if start >= node.end:
        if node.right:
            return helper(node.right, start, end)
        else:
            node.right = TreeNode(start, end)
            return True
    elif end <= node.start:
        if node.left:
            return helper(node.left, start, end)
        else:
            node.left = TreeNode(start, end)
            return True
    else:
        return False


class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.root:
            self.root = TreeNode(start, end)
            return True

        return helper(self.root, start, end)

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
