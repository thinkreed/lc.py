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
        fake_head = ListNode(-1)
        fake_head.next = head
        current = head
        previous = fake_head

        while current:
            if current.val == val:
                previous.next = current.next
            else:
                previous = previous.next
            current = current.next

        return fake_head.next

    def remove_elements(self, head, val):
        while head and head.val == val:
            head = head.next

        current = head

        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return head
