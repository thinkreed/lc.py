# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        count = 0

        while cur and count != k:
            cur = cur.next
            count += 1

        if count == k:
            cur = self.reverseKGroup(cur, k)

            while count > 0:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                count -= 1

            head = cur

        return head
