# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small_node = ListNode(0)
        small_head = small_node

        large_node = ListNode(1)
        large_head = large_node

        while head:
            if head.val < x:
                small_node.next = head
                small_node = small_node.next
            else:
                large_node.next = head
                large_node = large_node.next

            head = head.next

        small_node.next = large_head.next
        large_node.next = None

        return small_head.next
