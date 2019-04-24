# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        p_iter = head
        p_next = None

        while p_iter:
            p_next = p_iter.next

            copy = RandomListNode(p_iter.label)
            p_iter.next = copy
            copy.next = p_next

            p_iter = p_next

        p_iter = head

        while p_iter:
            if p_iter.random:
                p_iter.next.random = p_iter.random.next

            p_iter = p_iter.next.next

        p_iter = head
        fake_head = RandomListNode(0)
        copy = None
        copy_iter = fake_head

        while p_iter:
            p_next = p_iter.next.next
            copy = p_iter.next
            copy_iter.next = copy
            copy_iter = copy
            p_iter.next = p_next
            p_iter = p_next

        return fake_head.next
