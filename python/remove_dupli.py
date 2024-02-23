class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Not in-place
def deleteDuplicates(head):
    if head is None:
        return head
    if head.next is None:
        return head
    new_head = None
    ptr1 = head.next
    previous = head
    ptr2 = None
    while ptr1.next is not None:
        if ptr1.val != previous.val:
            if new_head is None:
                new_head = ListNode(previous.val)
                ptr2 = new_head
            else:
                new_node = ListNode(previous.val)
                ptr2.next = new_node
                ptr2 = new_node
        previous = ptr1
        ptr1 = ptr1.next
    if previous.val != ptr1.val:
        if new_head is None:
            new_head = ListNode(previous.val)
            new_head.next = ListNode(ptr1.val)
        else:
            ptr2.next = ListNode(previous.val)
            ptr2 = ptr2.next
            ptr2.next = ListNode(ptr1.val)
    else:
        if new_head is None:
            new_head = ListNode(previous.val)
        else:
            ptr2.next = ListNode(previous.val)
    return new_head


head = ListNode(1, ListNode(2, ListNode(3)))
head = deleteDuplicates(head)
current = head
while current.next is not None:
    print(current.val)
    current = current.next
print(current.val)
