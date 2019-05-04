class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        seen = set()

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num != '.':
                    exp = '(' + num + ')'

                    r_exp = exp + str(i)

                    if r_exp in seen:
                        return False

                    seen.add(r_exp)

                    c_exp = str(j) + exp

                    if c_exp in seen:
                        return False

                    seen.add(c_exp)

                    rc_exp = str(i // 3) + exp + str(j // 3)

                    if rc_exp in seen:
                        return False

                    seen.add(rc_exp)

        return True
