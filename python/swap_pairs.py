class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head):
    if head is None:
        return head
    elif head.next is None:
        return head
    current = head
    next_node = current.next
    previous = None
    while current.next is not None:
        if current is head:
            temp = next_node.next
            next_node.next = current
            current.next = temp
            previous = current
            current = temp
            head = next_node
        else:
            temp = next_node.next
            next_node.next = current
            current.next = temp
            previous = current
            current = temp
            if current is None:
                return head
        next_node = current.next
        previous.next = next_node
    previous.next = current
    return head
