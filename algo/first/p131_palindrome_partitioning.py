class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def helper(str, index):
            if index == len(str):
                res.append(list(path))
                return
            for i in range(index, len(str)):
                left = index
                right = i
                while left < right and str[left] == str[right]:
                    left += 1
                    right -= 1

                if left >= right:
                    path.append(str[index:i + 1])
                    helper(str, i + 1)
                    path.pop()

        res = []
        path = []
        helper(s, 0)
        return res
