class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        result = []
        member_dict = {}
        for i, number in enumerate(B):
            member_dict[number] = i

        for number in A:
            if number in member_dict:
                result.append(member_dict[number])

        return result
