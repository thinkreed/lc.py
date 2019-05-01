# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head and head.next:
            nn_node = head.next.next
            res_head = head.next
            head.next = nn_node
            res_head.next = head
        else:
            return head

        cur = head.next
        prev = head

        while cur and cur.next:
            next_next_node = cur.next.next
            tmp = cur.next
            cur.next = next_next_node
            tmp.next = cur
            prev.next = tmp
            prev = cur
            cur = next_next_node

        return res_head
