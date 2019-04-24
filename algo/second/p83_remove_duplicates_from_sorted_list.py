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
            return None

        p = head
        q = head

        while p and q:
            while q:
                if q.val != p.val:
                    break
                q = q.next

            p.next = q
            p = q

        return head
