from collections import deque


class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """

        def check_diff(current, next):
            diffs = 0
            for i in range(len(current)):
                if current[i] != next[i]:
                    diffs += 1
            return diffs == 1

        q = deque()
        q.append([start, start, 0])
        while q:
            cur, last, step = q.popleft()
            if cur == end:
                return step

            for item in bank:
                if check_diff(cur, item) and item != last:
                    q.append([item, cur, step + 1])

        return -1
