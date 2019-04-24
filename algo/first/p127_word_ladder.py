from collections import deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        q = deque([[beginWord, 1]])
        while q:
            word, w_len = q.popleft()
            if word == endWord:
                return w_len

            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    n_word = word[:i] + char + word[i + 1:]
                    if n_word in wordList:
                        wordList.remove(n_word)
                        q.append([n_word, w_len + 1])

        return 0
