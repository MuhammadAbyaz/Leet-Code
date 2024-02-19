class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(self, head, val: int):
    if head is None:
        return None
    elif head.next is None:
        if head.val == val:
            head = head.next
            return head
        else:
            return head
    current: ListNode = head
    previous = None
    while current.next is not None:
        if current.val == val:
            if previous is None:
                head = current.next
            else:
                previous.next = current.next
            current = current.next
        else:
            previous = current
            current = current.next
    if current.val == val:
        if previous is None:
            head = current.next
            return head
        else:
            previous.next = current.next
    return head
