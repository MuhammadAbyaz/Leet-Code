class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(self, lists: list[ListNode]) -> ListNode | None:
    if len(lists) == 0 or (len(lists) == 1 and not lists[0]):
        return None
    res = []
    for arr in lists:
        current = arr
        while current:
            res.append(current.val)
            current = current.next
    if res:
        res.sort()
        head = ListNode(val=res[0])
        current = head
        for i in range(1, len(res)):
            newNode = ListNode(val=res[i])
            current.next = newNode
            current = current.next
        return head
    else:
        return None
