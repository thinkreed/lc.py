class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        res = 0
        len_dict = {0: 0}
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)

            if '.' in name:
                res = max(res, len_dict[depth] + len(name))
            else:
                len_dict[depth + 1] = len_dict[depth] + len(name) + 1

        return res
