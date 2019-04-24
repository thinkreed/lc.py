# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = self
        p.next = head

        while p.next and p.next.next:
            odd = p.next
            even = odd.next

            p.next, even.next, odd.next = even, odd, even.next
            p = odd

        return self.next
