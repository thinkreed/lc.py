# parent node for i : floor((i - 1) / 2)
# left child node for i: 2 * i + 1
# right child node for i: 2 * i + 2

def heapify(elements, start, end):
    root_index = start
    while True:
        # assume the left child is the bigger child
        bigger_child_index = 2 * root_index + 1
        # whether out of elements index
        if bigger_child_index > end:
            break
        # assign the bigger child index to bigger_child_index
        if bigger_child_index + 1 <= end and elements[bigger_child_index] < elements[bigger_child_index + 1]:
            bigger_child_index = bigger_child_index + 1

        # if root is smaller than child, swap it
        if elements[root_index] < elements[bigger_child_index]:
            elements[root_index], elements[bigger_child_index] = elements[bigger_child_index], elements[root_index]
            root_index = bigger_child_index
        else:
            # the root is the biggest
            break


def heap_sort(elements):
    # from last parent node in the elements, make parent node bigger than children
    for i in range((len(elements) - 2) // 2, -1, -1):
        heapify(elements, i, len(elements) - 1)

    # from the end of the list, every time put the biggest value to the end, after put adapt the heap, make list[0] the
    # biggest
    for i in range(len(elements) - 1, 0, -1):
        elements[0], elements[i] = elements[i], elements[0]
        heapify(elements, 0, i - 1)


def test():
    elements = [9, 7, 4, 6, 3, 5, 8, 2, 0, 1]
    print(elements)
    heap_sort(elements)
    print(elements)


test()
