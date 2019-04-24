class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        s = []

        for asteroid in asteroids:
            while len(s) > 0 and 0 < s[-1] < -asteroid:
                s.pop()

            if len(s) == 0 or asteroid > 0 or s[-1] < 0:
                s.append(asteroid)
            elif asteroid < 0 and s[-1] == -asteroid:
                s.pop()

        return s
