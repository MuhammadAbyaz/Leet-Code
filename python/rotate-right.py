class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def rotateRight(head: ListNode, k: int) -> ListNode | None:
    if not head or not head.next:
        return head
    curr = head
    length = 0
    while curr:
        length += 1
        curr = curr.next
    k %= length
    if k == 0:
        return head
    ptr1 = head
    ptr2 = head
    for _ in range(k):
        ptr2 = ptr2.next
    while ptr2.next is not None:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    temp = ptr1.next
    ptr1.next = None
    ptr2.next = head
    head = temp
    return head
