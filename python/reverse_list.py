def reverseList(self, head):
    if head is None:
        return None
    if head.next is None:
        return head
    previous = current
    current = head
    nextNode = current.next
    while current.next is not None:
        if current == head:
            current.next = None
            current = nextNode
        else:
            current.next = previous
            previous = current
        nextNode = current.next
        current = current.next
    current.next = previous
    head = current
