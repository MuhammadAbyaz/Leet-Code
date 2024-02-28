class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution by reversing the list
def reverse(head):
    current = head
    nextNode = current.next
    previous = None
    while current.next is not None:
        current.next = previous
        previous = current
        current = nextNode
        nextNode = current.next
    current.next = previous
    head, current = current, head
    return head


def removeNthFromEnd(head, n):
    if head is None:
        return None
    if head.next is None:
        head = None
        return head
    head = reverse(head)
    if n == 1:
        head = head.next
        head = reverse(head)
        return head
    current = head
    for _ in range(n - 2):
        current = current.next
    current.next = current.next.next
    head = reverse(head)
    return head


head = ListNode(1, ListNode(2))
head = removeNthFromEnd(head, 1)
current = head
while current.next is not None:
    print(current.val)
    current = current.next
print(current.val)
