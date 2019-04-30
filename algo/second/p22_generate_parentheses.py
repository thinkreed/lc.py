class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        res = []

        def helper(cur, left, right):
            if right == n:
                res.append(cur)

            if left > right:
                if left < n:
                    helper(cur + '(', left + 1, right)
                if right < n:
                    helper(cur + ')', left, right + 1)
            elif left == right:
                if left < n:
                    helper(cur + '(', left + 1, right)

        helper('(', 1, 0)
        return res
