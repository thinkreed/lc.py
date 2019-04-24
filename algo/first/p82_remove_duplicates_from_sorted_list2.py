# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        fast = head
        slow = dummy

        slow.next = fast

        while fast:
            while fast.next and fast.val == fast.next.val:
                fast = fast.next

            if slow.next != fast:
                slow.next = fast.next
                fast = slow.next
            else:
                slow = slow.next
                fast = fast.next

        return dummy.next
