class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.m_stack = []
        self.s = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s.append(x)

        if len(self.m_stack) == 0:
            self.m_stack.append(x)
        elif self.m_stack[-1] >= x:
            self.m_stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if len(self.s) == 0:
            return

        if self.top() == self.m_stack[-1]:
            self.m_stack.pop()

        self.s.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.s[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.m_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
