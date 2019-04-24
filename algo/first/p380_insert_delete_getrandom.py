import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index = {}
        self.nums = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.index:
            return False
        self.index[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.index:
            return False
        val_index = self.index[val]
        last_element = self.nums[-1]
        self.nums[val_index] = last_element
        self.index[last_element] = val_index
        self.nums.pop()
        self.index.pop(val)
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.nums)
