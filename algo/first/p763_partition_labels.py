class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if not S or len(S) == 0:
            return None

        result = []
        char_map = {}

        for i, s in enumerate(S):
            char_map[s] = i

        substring_last = 0
        substring_start = 0

        for i, s in enumerate(S):
            substring_last = max(substring_last, char_map[s])

            if substring_last == i:
                result.append(substring_last - substring_start + 1)
                substring_start = substring_last + 1

        return result
