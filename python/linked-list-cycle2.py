class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(head: ListNode) -> ListNode | None:
    if head is not None and head.next is not None:
        ptr1 = head
        ptr2 = head
        while ptr2 is not None and ptr2.next is not None:
            ptr2 = ptr2.next.next
            ptr1 = ptr1.next
            if ptr1 == ptr2:
                break
        else:
            return None
        ptr1 = head
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1
    return None
