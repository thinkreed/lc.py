class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            self.dict.setdefault(len(word), []).append(word)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for candidate in self.dict.get(len(word), []):
            difference = 0
            for i in range(len(word)):
                if candidate[i] != word[i]:
                    difference += 1
            if difference == 1:
                return True

        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
