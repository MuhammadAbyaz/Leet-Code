def reverseKGroup(head, k):
    current = head
    length = 0
    head_node = head
    while head_node is not None:
        length += 1
        head_node = head_node.next
    length += 1

    if length % k != 0:
        length -= 1
    while length != 0:
        previous = current
        next_node = current.next
        temp_head = current
        for i in range(k):
            if current == head:
                current.next = None
                current = next_node
            else:
                current.next = previous
                previous = current
                current = next_node
            next_node = current.next
        temp_tail = temp_head
        if i > 0:
            temp_tail.next = previous
            temp_tail = temp_head
            temp_tail.next = current
        length -= k
