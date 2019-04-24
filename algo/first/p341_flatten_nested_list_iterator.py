# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.s = [[nestedList, 0]]

    def next(self):
        """
        :rtype: int
        """
        self.hasNext()
        l, i = self.s[-1]
        self.s[-1][1] += 1
        return l[i].getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.s:
            l, i = self.s[-1]
            if i == len(l):
                self.s.pop()
            else:
                val = l[i]
                if val.isInteger():
                    return True
                self.s[-1][1] += 1
                self.s.append([val.getList(), 0])

        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
