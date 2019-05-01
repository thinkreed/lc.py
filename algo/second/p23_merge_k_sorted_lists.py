from Queue import PriorityQueue


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        dummy = ListNode(None)

        node = dummy

        queue = PriorityQueue()

        for head in lists:
            if head:
                queue.put((head.val, head))

        while queue.qsize() > 0:
            node.next = queue.get()[1]
            node = node.next
            if node.next:
                queue.put((node.next.val, node.next))

        return dummy.next
