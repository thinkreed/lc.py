"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomList(self, head):
        if head == None:
            return None
        Start = Node(head.val, None, None)
        if head.next == None:
            if head.random != None:
                Start.random = Start
            return Start
        Pointer1 = head
        Counter = 0
        Dict = {}
        while Pointer1 != None:
            New = Node(Pointer1.val, None, None)
            if Pointer1.val not in Dict:
                Dict[Pointer1.val] = {}
            if Counter not in Dict[Pointer1.val]:
                Dict[Pointer1.val][Counter] = []
            Dict[Pointer1.val][Counter].append(New)
            if Counter == 0:
                Start = New
                Pointer2 = New
            else:
                Pointer2.next = New
                Pointer2 = Pointer2.next
            Pointer1 = Pointer1.next
            Counter += 1
        Pointer1 = head
        Pointer2 = Start
        while Pointer1 != None:
            if Pointer1.random != None:
                Goal = Pointer1.random
                if len(Dict[Goal.val]) == 1:
                    Length = list(Dict[Goal.val])[0]
                    if len(Dict[Goal.val][Length]) == 1:
                        Pointer2.random = Dict[Goal.val][Length][0]
            Pointer1 = Pointer1.next
            Pointer2 = Pointer2.next
        return Start

        """
        :type head: Node
        :rtype: Node
        """