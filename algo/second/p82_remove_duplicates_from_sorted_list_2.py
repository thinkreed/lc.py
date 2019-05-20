# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = ListNode(-1)
        cur.next = head
        head = cur

        while cur.next:
            next = cur.next

            while next and cur.next.val == next.val:
                next = next.next

            if next != cur.next.next:
                cur.next = next
            else:
                cur = cur.next

        return head.next
