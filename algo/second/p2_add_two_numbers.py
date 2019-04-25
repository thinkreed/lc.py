# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        node = head
        carry = 0

        while l1 and l2:
            val = l1.val + l2.val + carry

            if val >= 10:
                val -= 10
                carry = 1
            else:
                carry = 0

            l1.val = val
            node.next = l1
            node = node.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            val = l1.val + carry

            if val >= 10:
                val -= 10
                carry = 1
            else:
                carry = 0

            l1.val = val
            node.next = l1
            node = node.next
            l1 = l1.next

        while l2:
            val = l2.val + carry

            if val >= 10:
                val -= 10
                carry = 1
            else:
                carry = 0

            l2.val = val
            node.next = l2
            node = node.next
            l2 = l2.next

        if carry:
            node.next = ListNode(carry)

        return head.next
