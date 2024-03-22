class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


# def oddEvenList(head: ListNode):
#     if head is not None and head.next is not None:
#         oddHead = None
#         evenHead = None
#         oddPtr = None
#         evenPtr = None
#         curr = head
#         idx = 1
#         while curr is not None:
#             if idx % 2 != 0:
#                 if oddHead is None:
#                     oddHead = ListNode(curr.val)
#                     oddPtr = oddHead
#                 else:
#                     oddPtr.next = ListNode(curr.val)
#                     oddPtr = oddPtr.next
#             else:
#                 if evenHead is None:
#                     evenHead = ListNode(curr.val)
#                     evenPtr = evenHead
#                 else:
#                     evenPtr.next = ListNode(curr.val)
#                     evenPtr = evenPtr.next
#             curr = curr.next
#             idx += 1
#         head = oddHead
#         oddPtr.next = evenHead
#         return head


# better approach
def oddEvenList(head: ListNode):
    if not head:
        return None
    oddHead = head
    oddTail = head
    evenHead = head.next
    evenTail = head.next
    while evenTail and evenTail.next is not None:
        oddTail.next = evenTail.next
        oddTail = oddTail.next
        evenTail.next = oddTail.next
        evenTail = evenTail.next
    oddTail.next = evenHead
    return oddHead


head = ListNode(2, ListNode(4, ListNode(6, ListNode(8, ListNode(10)))))
head = oddEvenList(head)
curr = head
while curr.next is not None:
    print(curr.val)
    curr = curr.next
print(curr.val)
