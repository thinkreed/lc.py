class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []

        for sorted_person in sorted((-person[0], person[1]) for person in people):
            result.insert(sorted_person[1], [-sorted_person[0], sorted_person[1]])

        return result
