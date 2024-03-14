class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head):
    if head is None:
        return None
    palindrome_list = []
    current = head
    while current.next is not None:
        palindrome_list.append(current.val)
        current = current.next
    palindrome_list.append(current.val)
    return palindrome_list == palindrome_list[::-1]
