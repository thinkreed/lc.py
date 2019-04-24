class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        ss = ''.join([str(i) for i in (board[0] + board[1])])
        sp = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
        seen, step = set(), 0
        cl, nl = [ss], []
        while cl:
            for cur in cl:
                if cur == '123450':
                    return step
                ind = cur.index('0')
                for pos in sp[ind]:
                    nsl = [ch for ch in cur]
                    nsl[ind], nsl[pos] = nsl[pos], nsl[ind]
                    next_str = ''.join(nsl)
                    if next_str not in seen:
                        seen.add(next_str)
                        nl.append(next_str)
            cl, nl = nl, []
            step += 1
        return -1
