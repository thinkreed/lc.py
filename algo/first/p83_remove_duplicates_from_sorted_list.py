# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        prev = head
        current = head.next
        duplicate_value = head.val
        while current:
            if current.val <= duplicate_value:
                prev.next = current.next
                current = current.next
            else:
                duplicate_value = current.val
                prev, current = current, current.next

        return head
