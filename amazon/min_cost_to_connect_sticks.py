
from heapq import heapify, heappush, heappop
class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        
         edge cases
         if not sticks or len(sticks)= 1:
            return 0
        
         
         
         min_cost = 0
         push all elements of the array into min heap O(n)
            pop two values
            val = val1 + val2
            min_cost += val 
            heappush(h, val)
            
        
            
        

        """
        if len(sticks) == 1:
            return 0
        
        h = sticks
        
        heapify(h)
        
        min_cost = 0
        while len(h) > 1:
            val1 = heappop(h)
            val2 = heappop(h)
            val = val1 + val2
            min_cost += val
            heappush(h, val)
        return min_cost
            
        