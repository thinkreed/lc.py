class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.prefix_dict = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.prefix_dict[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        sumary = 0
        for key, value in self.prefix_dict.items():
            if key.startswith(prefix):
                sumary += value

        return sumary

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
