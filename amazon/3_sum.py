class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        
         [-1, 0, 1, 2, -1, -4],
         
         we sort an array  N logN
         
         [-4, -1, -1, 0, 1, 2]
           i   j            k
               i  j
              
         res is set() add list   
              
              
         n = len(nums)
         one for loop i from 0 up to n-2
         j = j+1
         k = n-1
         one while loop j < k
         we make a sum if it's less than zero we increment j 
         if iit's greater than zero we decrement k
         
         complexity O(N^3) and O(1) time
         
         2nd approach use dic  O(n^2) and O(n) time
         
        
        """
        if not nums or len(nums) < 3:
            return []
            
        n = len(nums)
        
        nums.sort()
        
        res = set()
        
        for i in range(n-2):
            j = i + 1
            k = n -1
            while j < k:
                curr = nums[i] + nums[j] + nums[k]
                if curr == 0:
                    t = tuple((nums[i], nums[j], nums[k]))
                    res.add(t)
                    j += 1
                    k -= 1
                elif curr < 0:
                    j += 1
                else:
                    k -= 1
        return res
                    
        