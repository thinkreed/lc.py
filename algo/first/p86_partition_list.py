# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        h1 = front = ListNode(0)
        h2 = back = ListNode(0)
        while head:
            if head.val < x:
                front.next = head
                front = front.next
            else:
                back.next = head
                back = back.next
            head = head.next
        back.next = None
        front.next = h2.next
        return h1.next
