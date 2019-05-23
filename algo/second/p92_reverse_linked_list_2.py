# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head

        pre = dummy

        for _ in range(m - 1):
            pre = pre.next

        start = pre.next
        then = start.next

        for _ in range(n - m):
            start.next = then.next
            then.next = pre.next
            pre.next = then
            then = start.next

        return dummy.next
