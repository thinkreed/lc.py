# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            s = head
            f = head.next
            while s is not f:
                s = s.next
                f = f.next.next
            return True
        except:
            return False
