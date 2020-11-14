class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        
          0,1,2,5,3,3,0
              i     j
              
          0,1,3,5,3,2,0
          
          0,1,3,0,2,3,5
          
          
          traverse from right to left if nums[i-1] < nums[i]
                pivot = nums[i-1]
                j = i
                while j < n and nums[i-1] < nums[j]:
                    j += 1
                nums[i-1], nums[j-1]  = nums[j-1], nums[i-1]
                
                nums[:] = nums[:i]  + nums[i:][::-1]
                
                
        
        
        
        """
        n  = len(nums)
        
        for i in range(n-1,0,-1):
            if nums[i] > nums[i-1]:
                j = i
                #  0,1,2,5,3,3,0  we have to find the 3 with n-2 indx
                while j < n and nums[i-1] < nums[j]:
                    j += 1
                # whiel loop is exhausted and we have to swap our pivot with nums[idx]
                nums[i-1], nums[j-1] = nums[j-1], nums[i-1]
                nums[:] = nums[:i] + nums[i:][::-1]
                return nums
        print(nums)
        nums.reverse()
        