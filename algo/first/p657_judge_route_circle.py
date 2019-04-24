class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        u_count = 0
        d_count = 0
        r_count = 0
        l_count = 0
        for move in moves:
            if move == 'U':
                u_count += 1
            elif move == 'D':
                d_count += 1
            elif move == 'R':
                r_count += 1
            elif move == 'L':
                l_count += 1
        return u_count == d_count and r_count == l_count

    def judge_circle(self, moves):
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
