from collections import deque


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        done = set()

        start_points = deque()
        start_points.append(0)

        while True:
            tmp_q = deque()
            for start in start_points:
                for word in wordDict:
                    if s[start:].startswith(word):
                        if s[start:] == word:
                            return True
                        new_start = start + len(word)
                        if new_start not in done:
                            done.add(new_start)
                            tmp_q.append(new_start)

            if not tmp_q:
                return False
            start_points = tmp_q
