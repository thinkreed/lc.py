from collections import defaultdict


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = defaultdict(list)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.dict[len(word)].append(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False

        if '.' not in word:
            return word in self.dict[len(word)]

        for item in self.dict[len(word)]:
            for index, c in enumerate(word):
                if c != item[index] and c != '.':
                    break
            else:
                return True

        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
