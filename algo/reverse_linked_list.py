class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_linked_list(head):
    if not head:
        return None
    if not head.next:
        return head

    # node now is the the head of the reversed list
    node = reverse_linked_list(head.next)
    # for now head.next points to the second node(i.e. the last node of the reversed list)
    # make head be the next of last node of the reversed list
    head.next.next = head
    head.next = None
    return node


def reverse_linked_list_iterative(head):
    # store the previous node of last loop
    node_prev = None
    # iterate over the linked list
    node_current = head
    # store the next node
    node_next = None

    while node_current:
        # store the next node
        node_next = node_current.next
        # reverse the link between current and next node
        node_current.next = node_prev
        # remember the operated node
        node_prev = node_current
        # move to next
        node_current = node_next

    # node_prev stores the last node of the old list(i.e. the head of the new list)
    return node_prev


def generate_linked_list(length):
    if length <= 0:
        return None
    head = ListNode(0)
    p = head
    for i in range(1, length):
        p.next = ListNode(i)
        p = p.next
    return head


def print_linked_list(head):
    if not head:
        print('invalid linked list')
    p = head
    while p:
        print(p.val)
        p = p.next


def test():
    head = generate_linked_list(6)
    print_linked_list(head)
    head = generate_linked_list(0)
    print_linked_list(head)
    head = generate_linked_list(1)
    print_linked_list(head)
    head = generate_linked_list(8)
    print_linked_list(head)
    print('reverse the linked list')
    head = reverse_linked_list(head)
    print_linked_list(head)
    head = reverse_linked_list_iterative(head)
    print_linked_list(head)


test()
