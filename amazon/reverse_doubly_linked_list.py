def reverse(head):
    if not head: return head

    curr = new_head = head
    
    while curr:
        curr.next, curr.prev = curr.prev, curr.next

        new_head = curr

        curr = curr.prev


    return new_head