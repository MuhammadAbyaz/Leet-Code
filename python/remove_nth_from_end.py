class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution by reversing the list
# def reverse(head):
#     current = head
#     nextNode = current.next
#     previous = None
#     while current.next is not None:
#         current.next = previous
#         previous = current
#         current = nextNode
#         nextNode = current.next
#     current.next = previous
#     head, current = current, head
#     return head


# def removeNthFromEnd(head, n):
#     if head is None:
#         return None
#     if head.next is None:
#         head = None
#         return head
#     head = reverse(head)
#     if n == 1:
#         head = head.next
#         head = reverse(head)
#         return head
#     current = head
#     for _ in range(n - 2):
#         current = current.next
#     current.next = current.next.next
#     head = reverse(head)
#     return head


# Two pointer solution


def removeNthFromEnd(head, n):
    if head is not None:
        if head.next is None:
            return None
        ptr1 = ListNode(-1, head)
        ptr2 = head
        for _ in range(n):
            ptr2 = ptr2.next
        while ptr2 is not None:
            ptr2 = ptr2.next
            ptr1 = ptr1.next
        if ptr1.next is head:
            head = head.next
            return head
        ptr1.next = ptr1.next.next
        return head
    return None
