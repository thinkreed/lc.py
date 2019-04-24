# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        current = root
        n = 0
        while current:
            n += 1
            current = current.next

        per_part_size = n // k
        number_of_larger_part = n % k

        parts = [per_part_size + 1] * number_of_larger_part + [per_part_size] * (k - number_of_larger_part)

        previous = None
        current = root

        for i, size in enumerate(parts):
            if previous:
                previous.next = None

            parts[i] = current

            for j in range(size):
                previous, current = current, current.next

        return parts
