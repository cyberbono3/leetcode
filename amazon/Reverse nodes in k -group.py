
"""
Use a dummy head, and

l, r : define reversing range

pre, cur : used in reversing, standard reverse linked linked list method

jump : used to connect last node in previous k-group to first node in following k-group
"""
def reverseKGroup(self, head, k):
    dummy = jump = ListNode(0)
    dummy.next = l = r = head
    
    while True:
        count = 0
        while r and count < k:   # use r to locate the range
            r = r.next
            count += 1
        if count == k:  # if size k satisfied, reverse the inner linked list
            prev, curr = r, l
            for _ in range(k):   # reverse ndoes
                curr.next = prev
                curr = curr.next
                prev = curr
            jump.next, jump, l = prev, l, r  # connect two k-groups
        else:
            return dummy.next