class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        if array is mutable
        
        
        works only with positive elements
        [1,-3,-4,-2,-2]
        
        
        we take index =  abs(x)
        if nums[index]  <0 :
            return index
        set nums[index] *= -1
        
         for x in nums:
                index = abs(x)
            if nums[index] < 0:
                return index
            nums[index]  *= -1
        
        
        ---------------------------------------------
        0 1 2 3 4
        3,4,1,4,2
        
        
        
        graph representation
        index -> val -> index
        build a graph index ->val -index and count indegree incoming edges
        
        0    1    2    3    4
        3 -> 4 -> 2 -> 1 -> 4  -> cycle to 2
        indegreee[4]  = 2 we return 4
        
        if not is in degre present return this node
        unin find
              
        
        
        """
        
       
    
            
        