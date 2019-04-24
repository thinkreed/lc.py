# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        revert = None
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next

            revert, revert.next, slow = slow, revert, slow.next

        if fast:
            slow = slow.next

        while revert and revert.val == slow.val:
            slow = slow.next
            revert = revert.next

        return not revert
