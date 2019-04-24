class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.end = False
        self.children = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.end = True

    def prefix_node(self, word):
        node = self
        for char in word:
            if char not in node.children:
                return None

            node = node.children[char]

        return node

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.prefix_node(word)

        if not node:
            return False
        else:
            return True if node.end else False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.prefix_node(prefix)
        return bool(node)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
