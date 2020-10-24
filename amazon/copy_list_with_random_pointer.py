 Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        dic = {}
        if not head:
            return None
        curr = head
        while curr:
            dic[curr] = Node(curr.val)
            curr = curr.next
            
        curr = head
        while curr:
            dic[curr].next = dic.get(curr.next, None)
            dic[curr].random = dic.get(curr.random, None)
            curr = curr.next
        return dic[head]
        