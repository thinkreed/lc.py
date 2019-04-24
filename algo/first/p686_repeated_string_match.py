class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        temp_string = ''
        count = 0

        while len(temp_string) < len(B):
            temp_string += A
            count += 1

        if B in temp_string:
            return count

        temp_string += A
        count += 1
        if B in temp_string:
            return count

        return -1

    def repeated_string_match(self, A, B):
        count = -(-len(B) // len(A))
        if B in (A * count):
            return count

        if B in (A * (count + 1)):
            return count + 1

        return -1
