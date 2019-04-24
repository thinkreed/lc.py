# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        def helper(head, tail):
            slow = head
            fast = head

            if head == tail:
                return None

            while fast != tail and fast.next != tail:
                fast = fast.next.next
                slow = slow.next

            node = TreeNode(slow.val)
            node.left = helper(head, slow)
            node.right = helper(slow.next, tail)
            return node

        if not head:
            return None

        return helper(head, None)
