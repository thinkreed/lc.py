class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        current_count_of_slices = 0
        total_count_of_slices = 0

        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                current_count_of_slices += 1
                total_count_of_slices += current_count_of_slices
            else:
                current_count_of_slices = 0

        return total_count_of_slices
