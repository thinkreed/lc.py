# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def merge(l1, l2):
            node = ListNode(0)
            p = node

            while l1 is not None and l2 is not None:
                if l1.val < l2.val:
                    p.next = l1
                    l1 = l1.next
                else:
                    p.next = l2
                    l2 = l2.next
                p = p.next

            if l1 is not None:
                p.next = l1

            if l2 is not None:
                p.next = l2

            return node.next

        if head is None or head.next is None:
            return head

        prev = None
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        h1 = self.sortList(head)
        h2 = self.sortList(slow)

        return merge(h1, h2)