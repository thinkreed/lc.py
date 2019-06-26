# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        dummy = ListNode(0)

        cur = head
        pre = dummy
        nex = None

        while cur:
            nex = cur.next

            while pre.next and pre.next.val < cur.val:
                pre = pre.next

            cur.next = pre.next
            pre.next = cur
            pre = dummy
            cur = nex

        return dummy.next
