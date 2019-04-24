class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_map = {char: index for index, char in enumerate(order)}
        words = [[order_map[char] for char in word] for word in words]

        return all(word1 <= word2 for word1, word2 in zip(words, words[1:]))
