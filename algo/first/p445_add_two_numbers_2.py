# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = []
        s2 = []

        while l1:
            s1.append(l1.val)
            l1 = l1.next

        while l2:
            s2.append(l2.val)
            l2 = l2.next

        sumary = 0
        node = ListNode(0)
        while s1 or s2:
            if s1:
                sumary += s1.pop()

            if s2:
                sumary += s2.pop()

            node.val = sumary % 10

            head = ListNode(sumary // 10)
            head.next = node
            node = head
            sumary //= 10

        return node.next if node.val == 0 else node
