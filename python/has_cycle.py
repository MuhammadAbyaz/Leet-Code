def hasCycle(self, head):
    current = head
    node_list = []
    while current:
        if current not in node_list:
            node_list.append(current)
        else:
            return True
        current = current.next
    return False
