lass Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        
        edge cases
        integer overflow
        num = 0 we have prod = 1
        

        
        ex2
          Input:  [1,2,0,4]
            
          prefix    1 1 2 1
        
    
      
        """
        n = len(nums)
        
        
        prefix = [1]*n
        
        prefix[0] = 1
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1] 
        
        suffix = [1]*n
        suffix[-1] = 1
        
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1]  * nums[i+1]
            
        for i in range(n):
            nums[i] = prefix[i] * suffix[i]
        return nums