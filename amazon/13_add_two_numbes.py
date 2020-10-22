# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        
        
         l1 = [2,4,3], l2 = [5,6,4]
         
         243
         564
         807
         
         
         
         [7, ]
        
        
        6 + 4
        
        10 % 10  = 0
        10 // 10 = 1
        
        
        6 + 3 
        9 %10 = 9
        
        
        """
        
        curr = dummy = ListNode(-1)
        
        
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            
            curr.next = ListNode(carry%10)
            carry = carry // 10
            curr = curr.next
        
        return dummy.next 
            