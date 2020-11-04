"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        dummy = Node(-1,None,head,None)
        prev = dummy
        stack = [head]
        
        while stack:
            curr = stack.pop()
            
            curr.prev = prev
            prev.next = curr
            prev = curr
            
            if curr.next:
                stack.append(curr.next)
                curr.next = None
            
            if curr.child:
                stack.append(curr.child)
                curr.child = None
                
        
        
        dummy.next.prev  = None
                
        
        return dummy.next
    