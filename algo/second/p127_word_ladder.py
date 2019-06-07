class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        from collections import deque
        if beginWord == endWord:
            return 1
        if len(beginWord) != len(endWord):
            return 0
        if endWord not in wordList:
            return 0
        wordList = set(wordList)
        letter_dict = set(list("".join(list(wordList))))
        N = len(beginWord)

        q_start = deque([(beginWord, 1)])
        q_end = deque([(endWord, 1)])
        visited_start = {beginWord: 1}
        visited_end = {endWord: 1}

        def helper(queue, visited, visited_other):
            word, level = queue.popleft()
            for i in xrange(len(word)):
                for c in letter_dict:
                    n_word = word[:i] + c + word[i + 1:]
                    if n_word not in wordList:
                        continue
                    if n_word in visited_other:
                        return level + visited_other[n_word]
                    else:
                        if n_word not in visited:
                            visited[n_word] = level + 1
                            queue.append((n_word, level + 1))
            return None

        while q_start and q_end:
            ans = helper(q_start, visited_start, visited_end)
            if ans:
                return ans
            ans = helper(q_end, visited_end, visited_start)
            if ans:
                return ans

        return 0

