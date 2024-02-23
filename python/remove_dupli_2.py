class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):
    if head is None:
        return head
    if head.next is None:
        return head
    new_head = None
    ptr2 = None
    ptr1 = head.next
    value = head.val
    count = 1
    while ptr1.next is not None:
        if ptr1.val == value:
            count += 1
        else:
            if count == 1:
                if new_head is None:
                    new_head = ListNode(value)
                    ptr2 = new_head
                else:
                    ptr2.next = ListNode(value)
                    ptr2 = ptr2.next
            count = 1
            value = ptr1.val
        ptr1 = ptr1.next

    if ptr1.val != value:
        if count == 1:
            if new_head is None:
                new_head = ListNode(value)
                ptr2 = new_head
                ptr2.next = ListNode(ptr1.val)
            else:
                ptr2.next = ListNode(value)
                ptr2 = ptr2.next
                ptr2.next = ListNode(ptr1.val)
        else:
            if new_head is None:
                new_head = ListNode(ptr1.val)
                ptr2 = new_head
            else:
                ptr2.next = ListNode(ptr1.val)
                ptr2 = ptr2.next
    return new_head


head = ListNode(
    1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5))))))
)
head = deleteDuplicates(head)
ptr1 = head
while ptr1.next is not None:
    print(ptr1.val)
    ptr1 = ptr1.next
print(ptr1.val)
