# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None

        while head.val == val:
            if not head.next:
                return None

            head = head.next

        previous = head
        current = head

        while current:
            if current.val == val:
                previous.next = current.next
            else:
                previous = current

            current = current.next

        return head
