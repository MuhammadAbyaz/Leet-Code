# def hasCycle(head):
#     current = head
#     node_list = []
#     while current:
#         if current not in node_list:
#             node_list.append(current)
#         else:
#             return True
#         current = current.next
#     return False


# Two pointer solution
def hasCycle(head):
    if head is not None and head.next is not None:
        ptr1 = head
        ptr2 = head.next.next
        while ptr2 is not None and ptr2.next is not None:
            if ptr2 == ptr1:
                break
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
        else:
            return False
        return True
