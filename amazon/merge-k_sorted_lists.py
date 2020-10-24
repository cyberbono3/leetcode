from heapq import heappop, heappush, heapify




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, val):
        node = ListNode(val)
        if not self.head:
            self.head = node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node
            
            
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        

        """
        
        #k the number of linked lists
        
        
        h = [(l.val , l) for l in lists if l]  # O(k)
        heapify(h) #  O(k)
        
        
        # overall complexity O(n + log n)  = O(n)
        
       
        dummy = curr = ListNode(-1)
            
        while h:
            val, node = heappop(h)       #O(log k)
            curr.next = ListNode(val)
            curr = curr.next
            
            if node.next:
                node = node.next
                heappush(h, (node.val, node)) #O(log k)
            
        return dummy.next

# TO DO debugging
l1, l2, l3 = LinkedList(), LinkedList(), LinkedList()
for v in [1,4,5]:
    l1.insert(v)
for v in [1,3,4]:
    l2.insert(v)
for v in [2,6]:
    l3.insert(v)

s = Solution()
lists = [l1,l2,l3]
print(s.mergeKLists(lists))



    
