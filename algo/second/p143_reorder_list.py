# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        p1 = head
        p2 = head

        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next

        preMiddle = p1
        preCurrent = p1.next

        while preCurrent.next:
            current = preCurrent.next
            preCurrent.next = current.next
            current.next = preMiddle.next
            preMiddle.next = current

        p1 = head
        p2 = preMiddle.next

        while p1 != preMiddle:
            preMiddle.next = p2.next
            p2.next = p1.next
            p1.next = p2
            p1 = p2.next
            p2 = preMiddle.next
