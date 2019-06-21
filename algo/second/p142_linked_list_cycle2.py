# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        dic = {}

        cur = head
        while cur:
            if cur not in dic:
                dic[cur] = cur
            else:
                return dic[cur]
            cur = cur.next

        return None
